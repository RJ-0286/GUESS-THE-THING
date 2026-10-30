// Guess the Thing - Interactive Game Engine, Subtle SFX, Settings, Autocomplete & Modal Controller

document.addEventListener("DOMContentLoaded", () => {
    // =========================================================
    // 1. SUBTLE WEB AUDIO SFX ENGINE & SETTINGS CONTROLLER
    // =========================================================
    const muteToggleEl = document.getElementById("settingMuteSfx");
    const hideHowToToggleEl = document.getElementById("settingHideHowTo");
    const sfxStatusIcon = document.getElementById("sfxStatusIcon");

    let isSfxMuted = localStorage.getItem("gtt_sfx_muted") === "true";
    let isHowToHidden = localStorage.getItem("gtt_hide_howto") === "true";
    let audioCtx = null;

    function getAudioCtx() {
        if (!audioCtx) {
            const Ctx = window.AudioContext || window.webkitAudioContext;
            if (Ctx) {
                audioCtx = new Ctx();
            }
        }
        return audioCtx;
    }

    function unlockAudio() {
        const ctx = getAudioCtx();
        if (!ctx || ctx.state !== "suspended") return;

        try {
            const buffer = ctx.createBuffer(1, 1, ctx.sampleRate);
            const source = ctx.createBufferSource();
            source.buffer = buffer;
            source.connect(ctx.destination);
            source.start(0);
            ctx.resume().catch(() => {});
        } catch (err) {
            ctx.resume().catch(() => {});
        }
    }

    function playTone(freqStart, freqEnd, durationSec, gainVal = 0.04, type = "sine", delaySec = 0) {
        if (isSfxMuted) return;
        const ctx = getAudioCtx();
        if (!ctx) return;

        const scheduleTone = () => {
            if (ctx.state !== "running") return;
            const now = ctx.currentTime + delaySec;
            try {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();

                osc.type = type;
                osc.frequency.setValueAtTime(freqStart, now);
                if (freqEnd && freqEnd !== freqStart) {
                    osc.frequency.exponentialRampToValueAtTime(freqEnd, now + durationSec);
                }

                gain.gain.setValueAtTime(0.001, now);
                gain.gain.linearRampToValueAtTime(gainVal, now + 0.008);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + durationSec);

                osc.connect(gain);
                gain.connect(ctx.destination);

                osc.start(now);
                osc.stop(now + durationSec + 0.01);
            } catch (err) {
                // Ignore audio context autoplay restrictions before first interaction
            }
        };

        if (ctx.state === "suspended") {
            ctx.resume().then(scheduleTone).catch(() => {});
        } else {
            scheduleTone();
        }
    }

    function playSfx(kind) {
        if (isSfxMuted) return;
        switch (kind) {
            case "click":
                playTone(520, 680, 0.04, 0.035, "sine");
                break;
            case "select":
                playTone(600, 840, 0.05, 0.04, "triangle");
                break;
            case "submit":
                playTone(440, 660, 0.08, 0.045, "sine");
                break;
            case "win":
                playTone(523.25, 523.25, 0.11, 0.05, "triangle", 0);
                playTone(659.25, 659.25, 0.11, 0.05, "triangle", 0.09);
                playTone(783.99, 783.99, 0.18, 0.055, "triangle", 0.18);
                break;
            case "wrong":
                playTone(330, 260, 0.12, 0.04, "sine", 0);
                break;
            case "tick":
                playTone(800, 750, 0.025, 0.025, "sine");
                break;
        }
    }

    function syncSettingsUI() {
        if (muteToggleEl) muteToggleEl.checked = isSfxMuted;
        if (hideHowToToggleEl) hideHowToToggleEl.checked = isHowToHidden;
        if (sfxStatusIcon) sfxStatusIcon.textContent = isSfxMuted ? "🔇" : "🔊";
    }

    syncSettingsUI();

    document.addEventListener("pointerdown", unlockAudio, true);
    document.addEventListener("keydown", unlockAudio, true);

    if (muteToggleEl) {
        muteToggleEl.addEventListener("change", () => {
            isSfxMuted = muteToggleEl.checked;
            localStorage.setItem("gtt_sfx_muted", isSfxMuted ? "true" : "false");
            syncSettingsUI();
            if (!isSfxMuted) playSfx("click");
        });
    }

    if (hideHowToToggleEl) {
        hideHowToToggleEl.addEventListener("change", () => {
            isHowToHidden = hideHowToToggleEl.checked;
            localStorage.setItem("gtt_hide_howto", isHowToHidden ? "true" : "false");
            syncSettingsUI();
            playSfx("click");
        });
    }

    // Attach subtle button click sounds across interactive controls
    document.addEventListener("click", (e) => {
        const btn = e.target.closest("button, .btn, .option, .movie-corner-btn, .lb-filter-btn");
        if (btn && !btn.classList.contains("sfx-submit")) {
            playSfx("click");
        }
    });

    // =========================================================
    // 2. THEME MANAGEMENT
    // =========================================================
    const themeToggle = document.getElementById("themeToggle");
    const savedTheme = localStorage.getItem("gtt_theme");

    function applyTheme(isLight) {
        if (isLight) {
            document.body.classList.add("light-mode");
            if (themeToggle) {
                themeToggle.innerHTML = "🌙 Dark";
                themeToggle.setAttribute("aria-pressed", "true");
            }
        } else {
            document.body.classList.remove("light-mode");
            if (themeToggle) {
                themeToggle.innerHTML = "☀️ Light";
                themeToggle.setAttribute("aria-pressed", "false");
            }
        }
    }

    applyTheme(savedTheme === "light");

    if (themeToggle) {
        themeToggle.addEventListener("click", () => {
            const isNowLight = !document.body.classList.contains("light-mode");
            applyTheme(isNowLight);
            localStorage.setItem("gtt_theme", isNowLight ? "light" : "dark");
        });
    }

    // =========================================================
    // 3. HOW TO PLAY MODAL (RESPECTS "HIDE HOW TO PLAY" SETTING)
    // =========================================================
    const movieArena = document.getElementById("movieArena");
    const howToPlayModalEl = document.getElementById("howToPlayModal");
    const guessInput = document.getElementById("guessInput");

    if (movieArena) {
        const roundState = movieArena.getAttribute("data-round-state");
        if (roundState === "win") {
            setTimeout(() => playSfx("win"), 120);
        } else if (roundState === "wrong_try" || roundState === "loss") {
            setTimeout(() => playSfx("wrong"), 100);
        }
    }

    if (movieArena && howToPlayModalEl) {
        const shouldAutoOpen = movieArena.getAttribute("data-auto-open-instructions") === "true";
        if (shouldAutoOpen && !isHowToHidden && typeof bootstrap !== "undefined" && bootstrap.Modal) {
            const modalInstance = bootstrap.Modal.getOrCreateInstance(howToPlayModalEl);
            modalInstance.show();
        }
    }

    // =========================================================
    // 4. GUESSING BOX — AUTOCOMPLETE DROPDOWN
    //    (Only opens when the player actually types, never auto-covers on enter!)
    // =========================================================
    const autocompleteList = document.getElementById("movieAutocompleteList");
    const catalogDataEl = document.getElementById("movieCatalogData");
    const guessForm = document.getElementById("movieGuessForm");
    let movieCatalog = [];

    if (guessForm) {
        guessForm.addEventListener("submit", () => {
            playSfx("submit");
        });
    }

    if (catalogDataEl) {
        try {
            movieCatalog = JSON.parse(catalogDataEl.textContent);
        } catch (err) {
            console.error("Failed to parse movieCatalogData:", err);
        }
    }

    if (guessInput && autocompleteList && movieCatalog.length > 0) {
        let activeIndex = -1;
        let currentMatches = [];

        const catConfig = {
            movies: { icon: "🎬", l1: "Dir", l2: "Star" },
            anime: { icon: "🎌", l1: "Creator", l2: "Main" },
            common_objects: { icon: "🔦", l1: "Area", l2: "Material" },
            superheroes: { icon: "🦸", l1: "Publisher", l2: "Identity" },
            games: { icon: "🎮", l1: "Dev", l2: "Hero" },
            characters: { icon: "👤", l1: "Medium", l2: "Universe" }
        };

        function renderDropdown(query) {
            const cleanQuery = (query || "").trim().toLowerCase();
            // Do NOT show dropdown if the input box is empty
            if (!cleanQuery) {
                autocompleteList.classList.add("d-none");
                autocompleteList.innerHTML = "";
                activeIndex = -1;
                return;
            }

            const startsWithMatches = [];
            const containsMatches = [];

            for (const item of movieCatalog) {
                const nameLower = (item.name || "").toLowerCase();
                const dirLower = (item.director || "").toLowerCase();
                const actorLower = (item.actor || "").toLowerCase();
                const yearStr = String(item.year || "");
                const genresStr = (Array.isArray(item.genres) ? item.genres.join(" ") : (item.genres || "")).toLowerCase();

                if (nameLower.startsWith(cleanQuery)) {
                    startsWithMatches.push(item);
                } else if (
                    nameLower.includes(cleanQuery) ||
                    dirLower.includes(cleanQuery) ||
                    actorLower.includes(cleanQuery) ||
                    yearStr.includes(cleanQuery) ||
                    genresStr.includes(cleanQuery)
                ) {
                    containsMatches.push(item);
                }
            }
            currentMatches = [...startsWithMatches, ...containsMatches].slice(0, 8);

            if (currentMatches.length === 0) {
                autocompleteList.classList.add("d-none");
                autocompleteList.innerHTML = "";
                activeIndex = -1;
                return;
            }

            activeIndex = -1;
            const currentCat = movieArena ? movieArena.getAttribute("data-category") : "movies";
            const cfg = catConfig[currentCat] || catConfig.movies;

            autocompleteList.innerHTML = currentMatches
                .map((m, idx) => {
                    const genresText = Array.isArray(m.genres) ? m.genres.join(", ") : (m.genres || "");
                    return `
                        <div class="autocomplete-item" role="option" data-index="${idx}" data-name="${m.name.replace(/"/g, '&quot;')}">
                            <div class="d-flex justify-content-between align-items-center flex-wrap gap-1">
                                <div class="fw-bold text-white autocomplete-movie-title">
                                    ${cfg.icon} ${m.name} <span class="text-info fw-semibold">(${m.year || ""})</span>
                                </div>
                                <div class="small text-secondary">
                                    ${m.rated ? `<span class="badge bg-secondary-subtle text-secondary-emphasis me-1">${m.rated}</span>` : ""}
                                    <span>${genresText}</span>
                                </div>
                            </div>
                            <div class="small text-secondary mt-1">
                                ${cfg.l1}: <span class="text-light">${m.director || "Unknown"}</span> • ${cfg.l2}: <span class="text-light">${m.actor || "Unknown"}</span> • ${m.studio || ""}
                            </div>
                        </div>
                    `;
                })
                .join("");

            autocompleteList.classList.remove("d-none");

            const items = autocompleteList.querySelectorAll(".autocomplete-item");
            items.forEach((item) => {
                item.addEventListener("mousedown", (e) => {
                    e.preventDefault();
                    const chosenName = item.getAttribute("data-name");
                    guessInput.value = chosenName;
                    autocompleteList.classList.add("d-none");
                    playSfx("select");
                    guessInput.focus();
                });
            });
        }

        function updateActiveItem(items) {
            items.forEach((item, i) => {
                if (i === activeIndex) {
                    item.classList.add("active");
                    item.scrollIntoView({ block: "nearest" });
                } else {
                    item.classList.remove("active");
                }
            });
        }

        guessInput.addEventListener("input", () => {
            renderDropdown(guessInput.value);
        });

        guessInput.addEventListener("focus", () => {
            if (guessInput.value.trim().length > 0) {
                renderDropdown(guessInput.value);
            }
        });

        guessInput.addEventListener("keydown", (e) => {
            const items = autocompleteList.querySelectorAll(".autocomplete-item");
            if (autocompleteList.classList.contains("d-none") || items.length === 0) {
                return;
            }

            if (e.key === "ArrowDown") {
                e.preventDefault();
                activeIndex = (activeIndex + 1) % items.length;
                updateActiveItem(items);
            } else if (e.key === "ArrowUp") {
                e.preventDefault();
                activeIndex = (activeIndex - 1 + items.length) % items.length;
                updateActiveItem(items);
            } else if (e.key === "Enter" && activeIndex >= 0 && items[activeIndex]) {
                e.preventDefault();
                const chosenName = items[activeIndex].getAttribute("data-name");
                guessInput.value = chosenName;
                autocompleteList.classList.add("d-none");
                activeIndex = -1;
                playSfx("select");
            } else if (e.key === "Escape") {
                autocompleteList.classList.add("d-none");
                activeIndex = -1;
            }
        });

        document.addEventListener("click", (e) => {
            if (!guessInput.contains(e.target) && !autocompleteList.contains(e.target)) {
                autocompleteList.classList.add("d-none");
            }
        });
    }

    // =========================================================
    // 5. LETTER PATTERN BUTTON & UNLOCKED CLUE SWITCHER (CLUE 1 <-> CLUE 2)
    // =========================================================
    const revealHintBtn = document.getElementById("revealHintBtn");
    const letterHintBox = document.getElementById("letterHintBox");
    if (revealHintBtn && letterHintBox) {
        revealHintBtn.addEventListener("click", () => {
            letterHintBox.classList.remove("d-none");
            revealHintBtn.disabled = true;
            revealHintBtn.innerHTML = "🔤 Pattern Shown";
            fetch("/api/use-hint", { method: "POST" }).catch(() => {});
        });
    }

    const singleClueBanner = document.getElementById("singleClueBanner");
    const activeClueBadge = document.getElementById("activeClueBadge");
    const singleClueText = document.getElementById("singleClueText");
    const prevClueBtn = document.getElementById("prevClueBtn");
    const nextClueBtn = document.getElementById("nextClueBtn");

    if (singleClueBanner && activeClueBadge && singleClueText) {
        const clueTabs = Array.from(singleClueBanner.querySelectorAll(".clue-tab-pill"));
        let currentClueIdx = parseInt(singleClueBanner.getAttribute("data-active-clue-index") || "0", 10);

        function selectClueByIndex(idx) {
            if (idx < 0 || idx >= clueTabs.length) return;
            currentClueIdx = idx;
            const targetTab = clueTabs[idx];
            const clueNum = targetTab.getAttribute("data-clue-num");
            const clueText = targetTab.getAttribute("data-clue-text");

            activeClueBadge.textContent = `💡 CLUE ${clueNum}`;
            singleClueText.textContent = clueText;

            clueTabs.forEach((tab, i) => {
                if (i === idx) {
                    tab.classList.add("active");
                } else {
                    tab.classList.remove("active");
                }
            });

            if (prevClueBtn) prevClueBtn.disabled = (idx <= 0);
            if (nextClueBtn) nextClueBtn.disabled = (idx >= clueTabs.length - 1);
        }

        if (clueTabs.length > 0) {
            // Initialize arrow button states
            if (prevClueBtn) prevClueBtn.disabled = (currentClueIdx <= 0);
            if (nextClueBtn) nextClueBtn.disabled = (currentClueIdx >= clueTabs.length - 1);

            clueTabs.forEach((tab, idx) => {
                tab.addEventListener("click", () => {
                    selectClueByIndex(idx);
                });
            });

            if (prevClueBtn) {
                prevClueBtn.addEventListener("click", () => {
                    if (currentClueIdx > 0) {
                        selectClueByIndex(currentClueIdx - 1);
                    }
                });
            }

            if (nextClueBtn) {
                nextClueBtn.addEventListener("click", () => {
                    if (currentClueIdx < clueTabs.length - 1) {
                        selectClueByIndex(currentClueIdx + 1);
                    }
                });
            }
        }
    }

    // =========================================================
    // 6. MOBILE / SCROLL "JUMP TO START" FLOATING PILL CONTROLLER
    // =========================================================
    const jumpToStartFab = document.getElementById("jumpToStartFab");
    const startGameBtn = document.getElementById("startGameBtn");

    if (jumpToStartFab && startGameBtn) {
        function updateJumpFabVisibility() {
            const rect = startGameBtn.getBoundingClientRect();
            const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
            // Show only when the Start Game button is further down below the visible screen
            const isStartBelowScreen = rect.top > viewportHeight - 20;
            if (isStartBelowScreen) {
                jumpToStartFab.classList.add("is-visible");
            } else {
                jumpToStartFab.classList.remove("is-visible");
            }
        }

        updateJumpFabVisibility();
        window.addEventListener("scroll", updateJumpFabVisibility, { passive: true });
        window.addEventListener("resize", updateJumpFabVisibility, { passive: true });

        jumpToStartFab.addEventListener("click", () => {
            startGameBtn.scrollIntoView({ behavior: "smooth", block: "center" });
            startGameBtn.classList.add("start-btn-pulse");
            setTimeout(() => {
                startGameBtn.classList.remove("start-btn-pulse");
            }, 1600);
        });
    }

    // =========================================================
    // 7. MAIN SCREEN LEADERBOARD CATEGORY FILTER
    // =========================================================
    const lbFilterBar = document.getElementById("homeLbFilterBar");
    if (lbFilterBar) {
        const filterBtns = lbFilterBar.querySelectorAll(".lb-filter-btn");
        const lbRows = document.querySelectorAll("#homeLbTable .lb-row");

        filterBtns.forEach((btn) => {
            btn.addEventListener("click", () => {
                filterBtns.forEach((b) => {
                    b.classList.remove("btn-primary", "active");
                    b.classList.add("btn-outline-secondary");
                });
                btn.classList.remove("btn-outline-secondary");
                btn.classList.add("btn-primary", "active");

                const selectedCat = (btn.getAttribute("data-cat") || "all").toLowerCase();
                lbRows.forEach((row) => {
                    const rowCat = (row.getAttribute("data-category") || "").toLowerCase();
                    if (selectedCat === "all" || rowCat === selectedCat) {
                        row.style.display = "";
                    } else {
                        row.style.display = "none";
                    }
                });
            });
        });
    }

    // =========================================================
    // 8. TIMER MODE COUNTDOWN CONTROLLER
    // =========================================================
    const roundTimerBadge = document.getElementById("roundTimerBadge");
    const roundTimerValue = document.getElementById("roundTimerValue");
    if (roundTimerBadge && roundTimerValue && roundTimerBadge.getAttribute("data-timer-active") === "true") {
        let timeLeft = 60;
        const interval = setInterval(() => {
            if (howToPlayModalEl && howToPlayModalEl.classList.contains("show")) {
                return;
            }
            timeLeft -= 1;
            roundTimerValue.textContent = String(Math.max(0, timeLeft));
            if (timeLeft <= 10 && timeLeft > 0) {
                roundTimerBadge.classList.remove("text-warning");
                roundTimerBadge.classList.add("text-danger");
                playSfx("tick");
            }
            if (timeLeft <= 0) {
                clearInterval(interval);
                const form = document.createElement("form");
                form.method = "POST";
                form.action = "/reveal-question";
                document.body.appendChild(form);
                form.submit();
            }
        }, 1000);
    }
});
