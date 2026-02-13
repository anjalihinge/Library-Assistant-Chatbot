# System Architecture

The Library Assistant Chatbot follows a simple client-server architecture.

## Components:
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Data Source: Predefined library data (books, authors, rules)

## Workflow:
1. User enters a query in the chat interface.
2. The request is sent to the Flask backend.
3. Backend matches keywords with predefined rules.
4. Relevant response is returned and displayed to the user.
