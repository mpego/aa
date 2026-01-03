// Counters Logic
const counters = {
    1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0
};

function updateCounter(id, change) {
    counters[id] += change;
    const element = document.getElementById(`counter-${id}`);
    element.textContent = counters[id];

    // Add pulse animation
    element.classList.remove('pulse');
    void element.offsetWidth; // Trigger reflow
    element.classList.add('pulse');
}

function updateCardColor(input) {
    const card = input.closest('.card');
    if (!card) return;

    // Convert Hex to RGBA with opacity
    const hex = input.value;
    const r = parseInt(hex.substring(1, 3), 16);
    const g = parseInt(hex.substring(3, 5), 16);
    const b = parseInt(hex.substring(5, 7), 16);

    card.style.background = `rgba(${r}, ${g}, ${b}, 0.7)`;
}

// Sound Logic
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playBeep(count = 1) {
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }

    const duration = 0.1; // seconds
    let frequency = 440; // Hz
    if (count > 1) {
        frequency = 1200;
    }
    const gap = 0.1; // seconds between beeps

    for (let i = 0; i < count; i++) {
        const oscillator = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(audioCtx.destination);

        oscillator.type = 'sine';
        oscillator.frequency.value = frequency;

        const startTime = audioCtx.currentTime + (i * (duration + gap));

        oscillator.start(startTime);
        oscillator.stop(startTime + duration);

        // Anti-pop ramp
        gainNode.gain.setValueAtTime(0.1, startTime);
        gainNode.gain.exponentialRampToValueAtTime(0.001, startTime + duration);
    }
}

// Timer Logic
const timerInput = document.getElementById('timer-duration');
let timeLeft = parseInt(timerInput.value) || 60;
let timerId = null;
let isRunning = false;

const timerDisplay = document.getElementById('timer-display');
const startBtn = document.getElementById('timer-start');
const pauseBtn = document.getElementById('timer-pause');
const resetBtn = document.getElementById('timer-reset');

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

function updateDisplay() {
    timerDisplay.textContent = formatTime(timeLeft);
    if (timeLeft <= 10) {
        timerDisplay.style.color = 'var(--danger)';
    } else if (timeLeft <= 15) {
        timerDisplay.style.color = 'var(--warning)';
    } else {
        timerDisplay.style.color = 'var(--text-primary)';
    }
}

function startTimer() {
    if (isRunning) return;

    // Ensure AudioContext is running on user interaction
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }

    isRunning = true;
    startBtn.disabled = true;
    startBtn.style.opacity = '0.5';
    pauseBtn.disabled = false;
    pauseBtn.style.opacity = '1';
    timerInput.disabled = true; // Disable input while running

    timerId = setInterval(() => {
        if (timeLeft > 0) {
            timeLeft--;
            updateDisplay();

            if (timeLeft === 15) {
                playBeep(1);
            } else if (timeLeft <= 10) {
                playBeep(1);
            }
        } else {
            clearInterval(timerId);
            isRunning = false;
            startBtn.disabled = false;
            startBtn.style.opacity = '1';
            timerInput.disabled = false;
            playBeep(3);
        }
    }, 1000);
}

function pauseTimer() {
    if (!isRunning) return;

    clearInterval(timerId);
    isRunning = false;
    startBtn.disabled = false;
    startBtn.style.opacity = '1';
    pauseBtn.disabled = true;
    pauseBtn.style.opacity = '0.5';
    timerInput.disabled = false;
}

function resetTimer() {
    pauseTimer();
    timeLeft = parseInt(timerInput.value) || 60;
    updateDisplay();
    // Reset visual state
    timerDisplay.style.color = 'var(--text-primary)';
}

// Event Listeners
startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pauseTimer);
resetBtn.addEventListener('click', resetTimer);
timerInput.addEventListener('input', () => {
    if (!isRunning) {
        timeLeft = parseInt(timerInput.value) || 60;
        updateDisplay();
    }
});

// Save/Load Logic
const saveBtn = document.getElementById('save-game');
const loadBtn = document.getElementById('load-game-btn');

function saveGame() {
    const gameState = {
        counters: counters,
        colors: {},
        names: {},
    };

    // Capture colors
    document.querySelectorAll('.card').forEach(card => {
        const id = card.dataset.id;
        gameState.colors[id] = card.style.background;
    });

    // Capture names
    document.querySelectorAll('.card-header input').forEach(input => {
        const id = input.id.replace('counter-name-', '');
        gameState.names[id] = input.value;
    });

    const outputBox = document.getElementById('game-state-json');
    outputBox.value = JSON.stringify(gameState);
    outputBox.style.display = 'block';
    outputBox.select();
}

function loadGame() {
    const inputBox = document.getElementById('game-state-json');
    try {
        const jsonContent = inputBox.value;
        if (!jsonContent) {
            alert('Please paste game JSON into the text box first.');
            return;
        }

        const gameState = JSON.parse(jsonContent);

        // Restore Counters
        if (gameState.counters) {
            Object.assign(counters, gameState.counters);
            for (const [id, value] of Object.entries(counters)) {
                const element = document.getElementById(`counter-${id}`);
                if (element) element.textContent = value;
            }
        }

        // Restore Colors
        if (gameState.colors) {
            for (const [id, color] of Object.entries(gameState.colors)) {
                const card = document.querySelector(`.card[data-id="${id}"]`);
                if (card && color) {
                    card.style.background = color;
                }
            }
        }

        // Restore Names
        if (gameState.names) {
            for (const [id, name] of Object.entries(gameState.names)) {
                const input = document.getElementById(`counter-name-${id}`);
                if (input) input.value = name;
            }
        }
    } catch (error) {
        console.error('Error loading game state:', error);
        alert('Invalid game state JSON. Please check the text box content.');
    }
}

saveBtn.addEventListener('click', saveGame);
loadBtn.addEventListener('click', loadGame);

// Settings Toggle Logic
const settingsToggle = document.getElementById('settings-toggle');
const settingsPanel = document.getElementById('settings-panel');

settingsToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    settingsPanel.classList.toggle('active');
});

// Close settings when clicking outside
document.addEventListener('click', (e) => {
    if (!settingsPanel.contains(e.target) && !settingsToggle.contains(e.target)) {
        settingsPanel.classList.remove('active');
    }
});

// Initialize
updateDisplay();
pauseBtn.disabled = true;
pauseBtn.style.opacity = '0.5';
