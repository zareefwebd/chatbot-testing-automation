# Manual Test Cases - Chatbot

Columns: TC_ID, Title, Precondition, Steps, Expected Result

TC001 | Health check | API up | GET /health | 200, status ok
TC002 | Greeting flow | User exists | POST /api/v1/chat {"message":"Hi"} | Bot replies with greeting
TC003 | Handling unknown intent | - | POST /api/v1/chat {"message":"random"} | Bot asks clarifying question
TC004 | API invalid payload | - | POST with missing fields | 4xx + error message
