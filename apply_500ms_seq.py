with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the map pin cycling logic in js/main.js with the exact 7-cohort 500ms sequence
old_start = "// 4. World Map Active Pin Cycling"
old_end = "// 5. Testimonial / Google Reviews Carousel"

start_idx = js.find(old_start)
end_idx = js.find(old_end)

if start_idx != -1 and end_idx != -1:
    new_script = """// 4. World Map Active Pin Cycling (Strict 500ms Step Cadence: 0ms, 500ms, 1000ms, 1500ms, 2000ms -> 2500ms Clear -> 3000ms Next)
    const mapWrapper = document.querySelector('.map-wrapper');
    const pins = [...document.querySelectorAll('.map-pin')];
    if (pins.length) {
        // 7 Non-Overlapping Globally Balanced Cohorts Covering All 35 Sovereign Jurisdictions
        const cohorts = [
            // Sequence 1 (Countries 1-5): Americas, NW Europe, N. Europe, E. Europe, E. Asia
            ['pin-usa', 'pin-uk', 'pin-sweden', 'pin-romania', 'pin-japan'],

            // Sequence 2 (Countries 6-10): SW Europe, C. Europe, Middle East, E. Asia, Oceania
            ['pin-portugal', 'pin-germany', 'pin-uae', 'pin-korea', 'pin-australia'],

            // Sequence 3 (Countries 11-15): N. Europe, W. Europe, SE Europe, S. Asia, E. Asia
            ['pin-norway', 'pin-luxembourg', 'pin-greece', 'pin-srilanka', 'pin-china'],

            // Sequence 4 (Countries 16-20): W. Europe, E. Europe, E. Africa, S. Asia, Oceania
            ['pin-ireland', 'pin-slovakia', 'pin-zanzibar', 'pin-bangladesh', 'pin-nz'],

            // Sequence 5 (Countries 21-25): W. Europe, Baltic, Mediterranean, Middle East, SE Asia
            ['pin-france', 'pin-latvia', 'pin-malta', 'pin-israel', 'pin-malaysia'],

            // Sequence 6 (Countries 26-30): W. Europe, C. Europe, S. Europe, S. Asia, SE Asia
            ['pin-netherlands', 'pin-austria', 'pin-italy', 'pin-india', 'pin-singapore'],

            // Sequence 7 (Countries 31-35): W. Europe, N. Europe, Alps, W. Africa, Indian Ocean
            ['pin-belgium', 'pin-denmark', 'pin-switzerland', 'pin-mali', 'pin-maldives']
        ];

        let cohortIndex = 0;
        let stepTimers = [];
        let mainTimer = null;
        let isRunning = false;
        let isHovered = false;

        const clearAllActivePins = () => {
            pins.forEach(p => p.classList.remove('active'));
        };

        const clearStepTimers = () => {
            stepTimers.forEach(t => clearTimeout(t));
            stepTimers = [];
        };

        const runSequence = () => {
            if (isHovered) return;
            clearStepTimers();
            clearAllActivePins();

            const currentCohort = cohorts[cohortIndex];
            if (!currentCohort) return;

            // 0 ms: Country 1 appears
            stepTimers.push(setTimeout(() => {
                if (isHovered) return;
                const el = document.getElementById(currentCohort[0]);
                if (el) el.classList.add('active');
            }, 0));

            // 500 ms: Country 2 appears (Country 1 remains)
            stepTimers.push(setTimeout(() => {
                if (isHovered) return;
                const el = document.getElementById(currentCohort[1]);
                if (el) el.classList.add('active');
            }, 500));

            // 1000 ms: Country 3 appears (Countries 1 and 2 remain)
            stepTimers.push(setTimeout(() => {
                if (isHovered) return;
                const el = document.getElementById(currentCohort[2]);
                if (el) el.classList.add('active');
            }, 1000));

            // 1500 ms: Country 4 appears (Countries 1, 2, and 3 remain)
            stepTimers.push(setTimeout(() => {
                if (isHovered) return;
                const el = document.getElementById(currentCohort[3]);
                if (el) el.classList.add('active');
            }, 1500));

            // 2000 ms: Country 5 appears (Countries 1, 2, 3, and 4 remain)
            stepTimers.push(setTimeout(() => {
                if (isHovered) return;
                const el = document.getElementById(currentCohort[4]);
                if (el) el.classList.add('active');
            }, 2000));

            // 2500 ms: Sequence clears. All elements (Countries 1 through 5) disappear simultaneously.
            stepTimers.push(setTimeout(() => {
                if (isHovered) return;
                clearAllActivePins();
            }, 2500));

            // 3000 ms: Next sequence begins!
            cohortIndex = (cohortIndex + 1) % cohorts.length;
            mainTimer = setTimeout(runSequence, 3000);
        };

        const startSequence = () => {
            if (isRunning) return;
            isRunning = true;
            runSequence();
        };

        const stopSequence = () => {
            isRunning = false;
            if (mainTimer) clearTimeout(mainTimer);
            mainTimer = null;
            clearStepTimers();
            clearAllActivePins();
        };

        if (mapWrapper) {
            mapWrapper.addEventListener('mouseenter', () => {
                isHovered = true;
                if (mainTimer) clearTimeout(mainTimer);
                mainTimer = null;
                clearStepTimers();
                clearAllActivePins();
            });
            mapWrapper.addEventListener('mouseleave', () => {
                isHovered = false;
                clearAllActivePins();
                runSequence();
            });
        }

        pins.forEach(pin => {
            pin.addEventListener('mouseenter', () => {
                isHovered = true;
                clearAllActivePins();
                pin.classList.add('active');
            });
            pin.addEventListener('mouseleave', () => {
                pin.classList.remove('active');
            });
        });

        startSequence();

        document.addEventListener('visibilitychange', () => {
            if (document.hidden) stopSequence();
            else startSequence();
        });
    }

    """
    js = js[:start_idx] + new_script + js[end_idx:]
    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("SUCCESS: Updated js/main.js with exact 500ms 7-cohort sequence and hover isolation!")
else:
    print("Could not find markers:", start_idx, end_idx)
