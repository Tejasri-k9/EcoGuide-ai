# 🌱 EcoGuide AI

**EcoGuide AI** is an intelligent sustainability assistant built using **Agentic AI + Retrieval-Augmented Generation (RAG)**. It provides document-grounded, interactive responses about sustainable living, environmental impact, and carbon footprint calculation.

This project is designed for **academic projects, internships, and hackathons**, demonstrating modern AI system design without relying on external APIs.

---

##  Key Features

1. Agentic AI Routing** – Dynamically routes user queries based on intent and conversation context
2. RAG (Retrieval-Augmented Generation)** – Answers are strictly grounded in a custom sustainability PDF
3. Conversation Memory** – Remembers selected topic (plastic, energy, water, etc.) for follow-up queries
4. Context-Aware Query Reformulation** – Improves retrieval relevance (e.g., `plastic impact` → `plastic impact` in PDF)
5. Carbon Footprint Calculator** – Estimates CO₂ emissions based on lifestyle inputs
6. No Hallucination** – Responses are sourced from the document or predefined logic only

---

##  Architecture Overview
![alt text](arch-image.png)
---

## Technologies Used

* **Python**
* **Agentic AI (Rule-based Agent Routing)**
* **RAG (PDF-based Retrieval-Augmented Generation)**
* **PyPDF2** (PDF text extraction)
* **State Management** (Conversation memory)

>  No external APIs, no LLM dependency — fully local & explainable.

---

##  Project Structure

```
EcoGuide-AI/
│
├── app.py                     # Main agent logic &conversation routing
├── carbon_calculator.py       # Carbon footprint calculation module
├── knowledge_base.py          # Predefined sustainability tips & mappings
├── pdf_retriever.py           # RAG module (PDF retrieval using PyPDF2)
├── prompts.py                 # Centralized prompt / response templates
├── data/
│   └── Sustainability_Knowledge_Base.pdf  # Custom sustainability document
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
```

---

![alt text](<Screenshot 2026-01-17 234743.png>)

##  Example Interactions

**User:** plastic  
**Bot:** Let’s talk about plastic. What would you like to know? (impact / examples / how to reduce)

**User:** impact  
**Bot:** Impact of Plastic (retrieved from sustainability PDF)

---
![alt text](<Screenshot 2026-01-17 224643.png>)
![alt text](<Screenshot 2026-01-17 220227.png>)

**User:** carbon  
**Bot:** Enter electricity, transport, plastic usage

**User:** 120, 8, 3  
**Bot:** Your Estimated Carbon Footprint: XX kg CO₂


---

##  Sustainability Knowledge Base

The assistant uses a **custom-generated sustainability PDF**, ensuring:
- High retrieval accuracy
- Domain relevance
- Demonstrable RAG implementation for evaluation

---

##  Why This Project Stands Out

- Demonstrates **real RAG**, not keyword responses
- Uses **agent-based decision making**
- Avoids hallucination by grounding all informational responses

---

## Future Improvements

- Semantic search using embeddings (FAISS)
- Confidence score for retrieved answers
- Web UI using Streamlit
- Source highlighting per response

---

##  Author

**Tejasri K**  
Computer Science & Engineering  
Passionate about AI for sustainability 

---

##  License

This project is for educational and academic use.

---

 *EcoGuide AI – Making sustainability understandable, interactive, and grounded.*

```
