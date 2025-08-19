# Chat With Your Books (Powered by RAG)

A friendly, modern chat interface that uses Retrieval-Augmented Generation (RAG) to answer questions grounded in your documents. It ships with a clean FastAPI backend and a delightful, responsive web UI. Pour in knowledge, ask away, and watch the magic happen ✨

## 🚀 Features

- **Intelligent Document Search**: Uses vector embeddings to find relevant document chunks
- **Modern Web Interface**: Beautiful, responsive design with smooth animations
- **Real-time Chat**: Interactive question-answering with instant responses
- **Source Attribution**: Shows which documents were used to generate answers
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Loading States**: Visual feedback during processing
- **Error Handling**: User-friendly error messages and graceful fallbacks

## 🏗️ Architecture

```
project/
├── app/
│   ├── __init__.py
│   ├── config.py          # Paths and env loading
│   ├── main.py            # FastAPI application entrypoint
│   ├── services/
│   │   ├── __init__.py
│   │   └── query_engine.py
│   └── static/
│       ├── index.html
│       ├── styles.css
│       └── script.js
├── scripts/
│   ├── __init__.py
│   └── create_database.py # Database initialization script
├── data/                  # Document storage
├── chroma/                # Vector database
├── requirements.txt
└── README.md
```

## 🛠️ Technology Stack

### Backend
- **Python 3.10+**: Core application logic
- **FastAPI**: Web framework for API endpoints
- **ChromaDB**: Vector database for document embeddings
- **Sentence Transformers**: Text embedding generation
- **LangChain**: RAG framework integration

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients and animations
- **JavaScript (ES6+)**: Interactive functionality
- **Font Awesome**: Icon library
- **Google Fonts**: Inter typography

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <your-project-folder>
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Initialize Database
```bash
python scripts/create_database.py
```

### 6. Run the Application
```bash
uvicorn app.main:app --reload --port 8000
```

The application will be available at `http://localhost:8000`

## 📚 Usage

### Adding Documents
1. Place your documents in the `data/` folder (subfolders are OK; files are discovered recursively)
2. Supported formats: PDF, TXT, DOCX
3. Run `python scripts/create_database.py` to process new documents

### Using the Chat Interface
1. Open your browser and navigate to the application
2. Type your question in the text area
3. Click "Ask Question" or press Enter
4. View the AI-generated answer and source documents
5. Ask follow-up questions for deeper exploration

### Example Questions
- "What are the main topics covered in the documents?"
- "Can you explain the key concepts?"
- "What are the main findings?"
- "How does this relate to [specific topic]?"

## 📖 Included Sample Dataset

- The example vector database created here is built from Herman Melville's classic: **Moby Dick (The Whale)** — a book of more than 500 pages. It's perfect for stress‑testing long‑context retrieval and seeing RAG in action on rich, narrative text.

You can swap in your own documents anytime by placing them in `data/` and re‑running the database script.

## 🖼️ Screenshots

Add your own screenshots to bring this to life. Place images in `docs/images/` and update the paths as needed.

![Main User Interface](docs/images/main-ui.png)
![Answer with Sources](docs/images/answer-sources.png)

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:
```env
OPENROUTER_API_KEY=your_key_here
```

### Customizing the Model
Edit `query_engine.py` to modify:
- Embedding model selection
- Similarity search parameters
- Response generation settings

### Customizing Ingestion (Chunking & Formats)
Edit `scripts/create_database.py` to modify:
- Chunk size and overlap
- Supported file formats (PDF, TXT, DOCX)
- Input directories under `data/`

## 📱 Interface Features

### Modern Design
- **Gradient Background**: Beautiful blue-to-purple gradient
- **Card Layout**: Clean, organized sections
- **Smooth Animations**: Hover effects and transitions
- **Responsive Grid**: Adapts to all screen sizes

### User Experience
- **Auto-resizing Input**: Textarea grows with content
- **Keyboard Shortcuts**: Enter to submit, Shift+Enter for new lines
- **Loading States**: Visual feedback during processing
- **Error Handling**: Clear error messages and recovery

### Accessibility
- **Semantic HTML**: Proper heading structure
- **Color Contrast**: High contrast for readability
- **Keyboard Navigation**: Full keyboard support
- **Screen Reader Friendly**: Proper ARIA labels

## 🧪 Testing

### Manual Testing
1. Test with various question types
2. Verify responsive design on different devices
3. Check error handling scenarios
4. Validate source attribution accuracy

### Performance Testing
- Monitor response times
- Check memory usage
- Test with large document collections

## 🚨 Troubleshooting

### Common Issues

**Database Connection Error**
```bash
# Ensure ChromaDB is properly initialized
python scripts/create_database.py
```

**Import Errors**
```bash
# Verify all dependencies are installed
pip install -r requirements.txt
```

**Port Already in Use**
```bash
# Change port in app/main.py or free the port
# macOS/Linux example for port 8000:
lsof -ti:8000 | xargs kill -9
# Windows example:
netstat -ano | findstr :8000
taskkill /PID <PID_FROM_ABOVE> /F
```

### Performance Issues
- Reduce chunk size in `scripts/create_database.py`
- Limit document collection size
- Use smaller embedding models

## 🔒 Security Considerations

- **Input Validation**: Sanitize user inputs
- **Rate Limiting**: Implement API rate limiting
- **Document Access**: Control document visibility
- **API Security**: Secure API endpoints

## 📈 Future Enhancements

- [ ] User authentication and document sharing
- [ ] Multiple document collections
- [ ] Advanced search filters
- [ ] Export conversations
- [ ] Integration with external APIs
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Document annotation tools

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **LangChain**: RAG framework
- **ChromaDB**: Vector database
- **Sentence Transformers**: Text embeddings
- **FastAPI**: Web framework
- **Font Awesome**: Icons
- **Google Fonts**: Typography

## 📞 Support

For questions, issues, or contributions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation

---

**Made with ❤️ for intelligent document exploration** 