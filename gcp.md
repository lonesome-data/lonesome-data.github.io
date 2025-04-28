graph TD
    subgraph "User Interface"
        UI[Web/Mobile App/Kiosk]
    end

    subgraph "Network Edge"
        CDN[Cloud CDN]
        LB[Global Load Balancer]
        WAF[Cloud Armor - WAF]
    end

    subgraph "API & Core Services"
        APIGW[API Gateway]
        Dialogflow[Dialogflow CX - Conversational AI Core & Basic KB]
        Translate[Cloud Translation API - Integrated]
        Backend[Cloud Run / Cloud Functions - Backend Microservices & Routing Logic]
        KBSearch[Vertex AI Search - Advanced Knowledge Base Search]
    end

    subgraph "Data & Analytics"
        Logging[Cloud Logging] --> BQ[BigQuery - Data Warehouse & Analytics]
        Firestore[Firestore - Session Data / Chat Logs - NoSQL]
        CloudSQL[Cloud SQL - Structured Application Data - Relational]
        GCS_KB[Cloud Storage - Knowledge Base Documents]
        VertexAI[Vertex AI - ML Model Training/Prediction for Analytics]
        PubSub[Pub/Sub - Asynchronous Tasks & Human Handoff Trigger]
    end

    subgraph "Security & Management"
        IAM[Identity & Access Management]
        IDPlatform[Identity Platform - Citizen Authentication]
        KMS[Key Management Service]
        SecMgr[Secret Manager]
        Monitor[Cloud Monitoring]
    end

    subgraph "External Systems"
        SLED_API[Existing SLED APIs/DBs]
        AgentDesk[Human Agent Desk/CRM]
    end

    %% Connections
    UI --> CDN --> LB --> WAF --> APIGW

    APIGW --> Dialogflow
    APIGW --> Backend
    APIGW --> KBSearch

    Dialogflow --> Translate
    Dialogflow --> Backend --> PubSub
    Dialogflow --> KBSearch --> GCS_KB

    Backend --> CloudSQL
    Backend --> Firestore
    Backend --> SLED_API
    Backend --> PubSub

    PubSub --> AgentDesk
    PubSub --> Backend %% For async processing triggers

    Logging --> BQ
    Backend --> Logging
    Dialogflow --> Logging

    BQ --> VertexAI
    VertexAI --> BQ

    %% Security Links
    APIGW -- Needs Auth --> IDPlatform/IAM
    Backend -- Uses Secrets --> SecMgr
    CloudSQL -- Encrypted By --> KMS
    Firestore -- Encrypted By --> KMS
    GCS_KB -- Encrypted By --> KMS
