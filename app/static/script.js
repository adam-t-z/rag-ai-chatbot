// RAG AI Chat Assistant - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const askBtn = document.getElementById('askBtn');
    const questionInput = document.getElementById('question');
    const answerEl = document.getElementById('answer');
    const sourcesEl = document.getElementById('sources');
    const loadingSpinner = document.getElementById('loadingSpinner');

    // Add enter key support (Shift+Enter for new line, Enter to submit)
    questionInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            askQuestion();
        }
    });

    askBtn.addEventListener('click', askQuestion);

    function setLoadingState(isLoading) {
        askBtn.disabled = isLoading;
        loadingSpinner.style.display = isLoading ? 'block' : 'none';
        askBtn.innerHTML = isLoading ? 
            '<div class="loading-spinner"></div> Processing...' : 
            '<i class="fas fa-paper-plane"></i> Ask Question';
    }

    function showAnswer(content, isError = false) {
        const className = isError ? 'error-message' : 'answer-text';
        answerEl.innerHTML = `<div class="${className}">${content}</div>`;
    }

    function showSources(sources) {
        if (!sources || sources.length === 0) {
            sourcesEl.innerHTML = `
                <div class="empty-state">
                    <i class="fas fa-info-circle" style="font-size: 2rem; color: #dee2e6; margin-bottom: 1rem;"></i>
                    <p>No sources found for this question.</p>
                </div>
            `;
            return;
        }

        sourcesEl.innerHTML = '';
        sources.forEach((chunk, i) => {
            const sourceDiv = document.createElement('div');
            sourceDiv.className = 'source-chunk';
            sourceDiv.innerHTML = `
                <div class="source-header">Source ${i + 1}</div>
                <div class="source-content">${chunk}</div>
            `;
            sourcesEl.appendChild(sourceDiv);
        });
    }

    async function askQuestion() {
        const question = questionInput.value.trim();
        if (!question) {
            showAnswer('Please enter a question!', true);
            return;
        }

        setLoadingState(true);
        showAnswer('Analyzing your question and searching through documents...');
        sourcesEl.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-search" style="font-size: 2rem; color: #dee2e6; margin-bottom: 1rem;"></i>
                <p>Searching through your documents...</p>
            </div>
        `;

        try {
            const response = await fetch('/query', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question }),
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();
            
            if (data.answer) {
                showAnswer(data.answer);
            } else {
                showAnswer('No answer found. Please try rephrasing your question.', true);
            }

            showSources(data.sources);

        } catch (err) {
            showAnswer(`Error: ${err.message}`, true);
            sourcesEl.innerHTML = `
                <div class="empty-state">
                    <i class="fas fa-exclamation-triangle" style="font-size: 2rem; color: #dee2e6; margin-bottom: 1rem;"></i>
                    <p>Unable to load sources due to an error.</p>
                </div>
            `;
        } finally {
            setLoadingState(false);
        }
    }

    // Auto-resize textarea
    questionInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = Math.min(this.scrollHeight, 200) + 'px';
    });

    // Focus on input when page loads
    questionInput.focus();
});




