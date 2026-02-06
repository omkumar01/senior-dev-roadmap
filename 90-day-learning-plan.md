# 90-Day Learning Plan: Foundations → Expert

**Assumptions:** Fast learner, strong basics. Goal: transition strong foundations to expert across Python, DSA, LLD, FastAPI, Docker, and System Design.

**Strategy:** Interleaved topics for retention, spaced repetition of cross-cutting themes (auth, testing, observability), and progression from code → classes → services → systems → scale → judgment.

---

## Week 1 — Advanced Python & OOP Deep Dive

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **1** | Python OOP core | Classes, Objects, methods (overriding, overloading), call by value/reference. **LLD:** Interface-driven design, encapsulation boundaries. | Implement a small domain with clear class boundaries. |
| **2** | OOP pillars | Inheritance, encapsulation, abstraction, polymorphism. **LLD:** SOLID principles (S, O, L). | Refactor one module applying SOLID. |
| **3** | SOLID & design thinking | SOLID (I, D), composition over inheritance, dependency injection. **Phase 1 LLD** mindset. | Design a service layer with DI (no framework). |
| **4** | Exceptions & control flow | Exception handling (Python). Memory model & execution flow. **LLD:** Error handling, validation. | Custom exception hierarchy + context managers. |
| **5** | Design patterns (behavior) | Strategy, Factory (simple + factory method). | Implement same feature with Strategy vs without. |
| **6** | Design patterns (creation) | Builder, Decorator. **Python:** Decorators (syntax, wraps, stacking). | Builder for a config object; decorator for logging/caching. |
| **7** | Design patterns & Python tools | Observer, Singleton (with caveats). **Python:** File handling, `pathlib`, `os`, `sys`. | Observer for event flow; critique Singleton use cases. |

---

## Week 2 — DSA Foundations & API Design Basics

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **8** | Linear structures | **DSA:** Arrays, Strings. Time & space complexity. **Python:** `collections`, `re` (regex). | 2 array/string problems; complexity analysis. |
| **9** | Hashing & lookup | **DSA:** Hash tables (dict/set). Caching algorithms: LRU, LFU. | Implement LRU cache from scratch; 1 hash-based problem. |
| **10** | Stacks & queues | **DSA:** Stack, Queues. **Python:** Using `list`, `collections.deque`. | Classic stack/queue problems (paranthesis, BFS-ready queue). |
| **11** | Trees & heaps | **DSA:** Tree, Heap. **Python:** Heapq usage. | Tree traversal (iterative + recursive); heap for top-K. |
| **12** | Graphs & recursion | **DSA:** Graph basics (repr, BFS/DFS), Recursion. | One graph problem; one recursion-to-iteration refactor. |
| **13** | Sorting & searching | **DSA:** Sorting (comparison + key algos), Searching (binary, etc.). | Implement 2 sorts; analyze when to use which. |
| **14** | API & service design | Controller–Service–Repository. DTO vs Entity. Pagination, filtering, API versioning. Idempotent APIs. | Design REST API for one resource (on paper/skeleton). |

---

## Week 3 — Python Ecosystem & Data Layer Foundations

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **15** | Package & modules | **Python:** Package manager – `pyproject.toml`. **Modules:** Pydantic, Requests, Json, logging. | Create a small package with `pyproject.toml`; structured logging. |
| **16** | Stdlib & concurrency | **Modules:** sys, os, pathlib, enum, csv, sqlite3, datetime/zoneinfo, threading. | Script using pathlib + datetime; simple threading example. |
| **17** | DB connectivity (drivers) | **DB:** SQLite, Postgres, Oracle, Mongo (pymongo). Connection patterns. | Minimal scripts: SQLite + one of Postgres/Mongo. |
| **18** | ORM & schema | **ORM:** SQLAlchemy (sync). **DB LLD:** Relational modeling, normalization vs denormalization. | One small schema with SQLAlchemy models; normalize a sample schema. |
| **19** | DB LLD deep | **DB LLD:** Indexing strategies, transactions & isolation levels, locking strategies, schema evolution. | Add indexes for sample queries; write a transaction with isolation. |
| **20** | Caching & sessions | **Caching:** Redis (keys, TTLs, invalidation). **Auth:** Basic, Token, Session. | Redis get/set/expire; simple session store. |
| **21** | Auth & JWT | **Auth:** JWT – pyjwt. **Security (roadmap):** Authentication vs Authorization, JWT internals. | Implement token issue + verify; explain header/payload/signature. |

---

## Week 4 — FastAPI Core & Layered Architecture

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **22** | ASGI & lifecycle | **FastAPI:** Core concepts. ASGI fundamentals (lifecycle, concurrency, Starlette). Request/Response, StreamingResponse, FileResponse. | Minimal FastAPI app with lifecycle awareness. |
| **23** | Routing & validation | Routing, APIRouter, route params, path vs query, path converters. **Pydantic v2:** BaseModel, field_validator, model_validate, model_dump, Annotated. | CRUD routes with path/query; Pydantic validators. |
| **24** | DI & lifespan | Dependency injection (Depends, Annotated, scopes, caching, teardown via yield). Lifespan vs startup/shutdown. | DB session as dependency with teardown. |
| **25** | OpenAPI & responses | OpenAPI (schema, enums, examples, tags, operation ids). Response models (read vs write, inclusion/exclusion, unions, generics). | Document one API with examples and tags. |
| **26** | Background & layout | Background tasks vs queue. **Layered architecture:** api/, services/, repositories/, models/, schemas/, core/, settings. **Middleware:** Starlette middlewares. | Restructure a small FastAPI app into layers. |
| **27** | REST & errors | **REST:** Resource modeling, pagination, filtering, sorting. **Error handling:** Custom exception handlers, error envelopes. | Paginated list endpoint; global exception handler. |
| **28** | Testing (Python + API) | **Testing:** Pytest. **FastAPI:** DB testing (transactional fixtures, ephemeral DBs, containers). Contract tests (OpenAPI), client/server compatibility. | Pytest suite for one service; one contract test. |

---

## Week 5 — FastAPI Async, Security & Data Layer

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **29** | Async correctness | Async/await (avoid blocking, threadpool where needed). Async drivers: asyncpg, motor, httpx.AsyncClient. | Convert one sync endpoint to async; use asyncpg or motor. |
| **30** | Cancellation & backpressure | Cancellation propagation, timeouts. Backpressure (streaming, chunked). Concurrency control (semaphores/limits). | Streaming response with backpressure; timeout on external call. |
| **31** | Auth in FastAPI | OAuth2 + JWT. Session vs token (cookie, CSRF). Password hashing (passlib/argon2), secure token storage. | OAuth2 flow + JWT issue/verify in FastAPI. |
| **32** | RBAC, ABAC & CORS | Role/scope (RBAC), Attribute-based (ABAC). CORS allowlists. Secret management (env, vaults, pydantic-settings). | Dependency that enforces RBAC; CORS config. |
| **33** | Security hardening | Rate limiting. Input sanitization, safe file uploads (size/type). HTTPS/TLS, HSTS. | Rate limiter middleware; file upload validation. |
| **34** | SQLAlchemy 2.0 & Alembic | SQLAlchemy 2.0 sync/async engines, session lifecycle, Unit of Work. **Migrations:** Alembic (autogenerate, revisions, offline/online). | Async engine + session; one Alembic migration. |
| **35** | MongoDB & transactions | MongoDB (motor), indexing, schema with Pydantic. **Transactions:** ACID, multi-document, idempotency keys. Connection pooling. **Caching:** Redis in FastAPI. | Motor + index; one transactional endpoint with idempotency. |

---

## Week 6 — APIs, Testing & Uvicorn

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **36** | WebSockets & SSE | WebSockets (auth, backpressure). SSE/streaming. **Roadmap:** WebSockets/SSE in communication. | WebSocket endpoint with auth; one SSE endpoint. |
| **37** | Versioning & testing | Versioning strategies. **Testing:** Performance tests, security tests. | Versioned route (e.g. /v1/); one load or security test. |
| **38** | Uvicorn & proxy | Uvicorn (workers, worker class, --http/--httptools/--kiio, uvloop, timeouts). Reverse proxy (nginx/traefik role). | Run with multiple workers; document proxy config. |
| **39** | Observability (logging) | **Structured logging:** Correlation IDs, request IDs, JSON logs. **Roadmap:** Observability foundations. | Middleware that adds request_id; JSON log format. |
| **40** | Metrics & tracing | **Metrics:** Prometheus/OpenTelemetry, RED/USE, custom business metrics. **Tracing:** OTel for FastAPI, DB, httpx. | Expose /metrics; one traced request end-to-end. |
| **41** | Health & operations | Health checks (liveness/readiness, DB/Redis). Feature toggles. Audit logging. **Roadmap:** Alerting strategies. | Liveness + readiness with DB check; simple feature flag. |
| **42** | Event streaming | Event streaming with Kafka. **Roadmap:** Message queues vs streams, Kafka fundamentals. | Produce/consume one event type with Kafka (or mock). |

---

## Week 7 — Docker Fundamentals

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **43** | Images | Base image, creating from scratch. Union filesystem, copy-on-write layers. Image versioning and tagging. **Roadmap:** Docker internals. | Build image from Dockerfile; inspect layers. |
| **44** | Containers | Create, start, stop, exec, rm. Detached/interactive. Resource limits. | Run container with limits; exec into running container. |
| **45** | Dockerfile (1) | Multi-stage build, minimizing image size. COPY vs ADD. ENTRYPOINT vs CMD. Build args vs env variables. | Multi-stage Dockerfile for a Python app. |
| **46** | Dockerfile (2) | Optimizing layer caching. Security best practices. **Performance:** Multi-stage, rebuild times, image size (alpine/slim/distroless), build cache. | Reduce image size; order instructions for cache. |
| **47** | Networking | Network types (bridge, host, none, custom). Ports (publishing vs exposing, mapping). Inter-container (DNS, isolation). | Two containers on custom network talking by name. |
| **48** | Storage | Volumes (named, anonymous). Bind mounts. Data persistence across recreation. Backup and migration of volumes. | App that persists data in a named volume. |
| **49** | Docker Compose | Multi-service app. Env variables, health checks. Networks and volumes in compose. Overrides, profiles. Production vs dev compose. | Compose file with app + DB + Redis + health checks. |

---

## Week 8 — Docker Advanced & Security

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **50** | Security | Least privilege (non-root, dropping capabilities). Image security (build secrets, no secrets in images, scanning). Preventing breakout (read-only FS, seccomp/AppArmor/SELinux basics). | Run as non-root; use build secrets. |
| **51** | Build system | BuildKit. Layer caching rules, deterministic builds. Context and .dockerignore. Build performance tuning. | BuildKit build; .dockerignore to shrink context. |
| **52** | Registry & images | Pushing/pulling. Private registries (Docker Hub limits, self-hosted, auth). Immutable tags. Multi-arch images. | Push to registry; use a tag strategy. |
| **53** | Debugging | Container logs, network issues, build failures, permission issues. docker logs, exec, inspect, top, stats, diff. | Debug a failing container using inspect/stats/logs. |
| **54** | Production Docker | Production best practices. **Roadmap:** Containers & Kubernetes (Docker internals recap). | Checklist: user, health, logging, resource limits. |
| **55** | System design – architecture | **Core architecture:** Monolith vs Microservices, modular monolith. Layered, Clean/Hexagonal. Event-driven systems. | Draw one monolith and one event-driven variant. |
| **56** | Communication & integration | REST vs GraphQL vs gRPC. Sync vs Async. Message queues vs streams. Kafka. **Recap:** WebSockets/SSE. | Compare REST vs gRPC for one use case. |

---

## Week 9 — Data at Scale & Scalability

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **57** | Data at scale | SQL vs NoSQL tradeoffs. CAP (practical). Sharding & partitioning. Replication. Read/write separation. | Choose SQL vs NoSQL for 2 scenarios; sketch sharding. |
| **58** | Scalability | Load balancing (L4 vs L7). Horizontal scaling. **Caching:** Redis, CDN. Cache invalidation strategies. Backpressure. | Design cache layer for an API; invalidation strategy. |
| **59** | Reliability | Circuit breaker, retries & timeouts, rate limiting. Bulkhead pattern. Graceful degradation. | Implement or diagram circuit breaker + retries. |
| **60** | Security & identity (consolidation) | **Roadmap:** Auth vs Authz, JWT, OAuth2, RBAC/ABAC, API security. **FastAPI:** Recap secret management, CORS. | One-page “security checklist” for an API. |
| **61** | Kubernetes intro | **K8s:** Architecture. Pods, Services, Ingress. ConfigMaps & Secrets. HPA / Autoscaling. | Deploy one app to local K8s (minikube/kind); use ConfigMap. |
| **62** | Observability & DevOps | **Roadmap:** Structured logging, RED/USE metrics, tracing. Alerting. Blue-green & canary deployments. **FastAPI:** Recap metrics, tracing, health. | Define RED metrics for one service; canary strategy. |
| **63** | Admin & cross-cutting | **FastAPI:** Admin backends. **Recap:** Layered architecture, testing strategy, observability. | Design admin API (or list endpoints) for one resource. |

---

## Week 10 — Advanced Patterns & Distributed Foundations

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **64** | CQRS & event sourcing | **Advanced patterns:** CQRS, Event sourcing. | Model one feature as CQRS; event-sourced aggregate sketch. |
| **65** | Saga & strangler | Saga pattern. Strangler pattern. API Gateway pattern. | Diagram saga for a cross-service flow; strangler steps. |
| **66** | Consistency & idempotency | **Distributed:** Consistency models. Exactly-once semantics. Idempotency design. **FastAPI/API:** Idempotency keys recap. | Design idempotent API for payments; consistency tradeoffs. |
| **67** | Clocks & ordering | Clock skew & ordering. Distributed locks. | When to use distributed locks; clock skew impact on ordering. |
| **68** | Engineering judgment (1) | Tradeoff analysis. Cost vs performance. When NOT to use microservices. | Document “microservices vs monolith” for one product. |
| **69** | Engineering judgment (2) | Simplification over time. Mentoring & design reviews. **Mental model:** Code → Classes → Services → Systems → Scale → Judgment. | Review a past design; list 3 simplifications. |
| **70** | Integration day 1 | **Python:** Full checklist scan – any missed modules (e.g. enum, csv, re). **DSA:** One problem per category (array, tree, graph, DP if applicable). | Solve 2–3 mixed problems; run full test suite. |

---

## Week 11 — Depth & Spaced Repetition

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **71** | OOP & design patterns recap | All design patterns (Strategy, Factory, Builder, Observer, Decorator, Singleton). SOLID. Composition vs inheritance. | Implement same behavior with 2 different patterns. |
| **72** | DSA & complexity | Arrays, hashing, stacks, queues, trees, graphs, recursion. Time/space. LRU/LFU. | 2 problems; write complexity and justify approach. |
| **73** | DB & transactions | Relational modeling, indexing, transactions, locking. SQLAlchemy 2.0, Alembic. Mongo indexing, multi-doc transactions. | Design schema change + migration; transaction boundaries. |
| **74** | Auth & security end-to-end | Basic, Token, Session, JWT. OAuth2, RBAC/ABAC. Rate limiting, sanitization, secrets. | End-to-end auth flow diagram; security checklist. |
| **75** | FastAPI production stack | Layers, DI, async, validation, OpenAPI. Testing (DB, contract, perf, security). Uvicorn, reverse proxy. | Checklist: “Production FastAPI” (config, auth, DB, tests). |
| **76** | Docker & Compose production | Images, Dockerfile, networking, volumes, Compose, security, BuildKit, registry, debugging. | Single “production Docker” checklist. |
| **77** | System design synthesis | Architecture patterns, communication, data at scale, scalability, reliability, security. K8s, observability, deployments. | One full system design (e.g. “design a URL shortener”). |

---

## Week 12 — Expert Consolidation & Final Stretch

| Day | Focus | Topics | Practice / Retention |
|-----|--------|--------|----------------------|
| **78** | Distributed systems deep | Consistency, exactly-once, idempotency, clocks, distributed locks. CQRS, event sourcing, Saga. | Explain to “someone else” (write or record) one distributed concept. |
| **79** | Advanced architecture | CQRS, event sourcing, Saga, Strangler, API Gateway. When to use each. | Match pattern to scenario (3 scenarios). |
| **80** | Senior mindset | Tradeoffs, cost vs performance, when not to microservices, simplification, design reviews. **Final mental model.** | Write a one-page “design review guide” for yourself. |
| **81** | Full stack review | From request to response: proxy → app → DB/cache → observability. Auth, errors, versioning. | Trace one request through your mental stack. |
| **82** | Checklist audit – Skills | **Skills-Checklist:** Tick every item (Advanced Python, Docker, FastAPI). Fill gaps with 30-min focus each. | Mark missed items; do one micro-session per gap. |
| **83** | Checklist audit – Roadmap | **Roadmap:** Phase 0→5. Ensure you can “explain, implement, justify” at least one item per section. | List weak spots; one implementation or explanation each. |
| **84** | Mock interview / design | Timed system design (30–45 min). Then LLD (one class/API design). | One system design + one LLD; self-grade. |
| **85** | Teaching & retention | Explain 3 topics to an imaginary junior: e.g. DI, circuit breaker, event sourcing. | Write or record 3 short explanations. |
| **86** | Performance & ops | RED/USE, tracing, alerting. Backpressure, rate limiting, timeouts. Docker resource limits, K8s HPA. | Define SLOs for one service; link to metrics/alerts. |
| **87** | Security end-to-end | Auth, Authz, JWT, OAuth2, RBAC/ABAC. Secrets, CORS, rate limiting, input validation. Image security, non-root containers. | Security one-pager for “deploying a new service”. |
| **88** | Integration project (optional) | Small project: FastAPI + Docker Compose + DB + Redis + structured logging + tests. | Build or extend one integrated app. |
| **89** | Final review – explain | Go through roadmap “expert” bar: explain, implement, justify. List any remaining gaps. | 5 bullet “I can explain/implement/justify” statements. |
| **90** | Plan recap & next steps | Recap 90 days. Set 3 concrete “next 30 days” goals (e.g. one system design per week, contribute to OSS). | Write your “from strong foundations to expert” summary. |

---

## Topic Coverage Index

### From Skills-Checklist.txt
- **Advanced Python:** OOP (classes, objects, methods, inheritance, encapsulation, abstraction, polymorphism), exception handling, DSA (string, array, linked list, stack, queues, hash tables, heap, sorting, searching, tree, graph, recursion), file handling, decorators, pyproject.toml, authentication (basic, token, session, JWT), DB (SQLite, Postgres, Oracle, Mongo), Redis, modules (Pydantic, Requests, Json, logging, sys, os, pathlib, enum, csv, sqlite3, datetime/zoneinfo, re, collections, threading), ORM (SQLAlchemy), Testing (Pytest).
- **Docker:** Images, containers, Dockerfile, networking, storage, Compose, security, performance, build system, registry, debugging, production.
- **FastAPI:** Core/ASGI, request/response, routing, DI, lifespan, Pydantic v2, OpenAPI, response models, background tasks, layered architecture, middleware, async, auth/security, data layer (SQLAlchemy 2.0, Alembic, Mongo, transactions, pooling, Redis), REST, errors, WebSockets, SSE, versioning, testing, Uvicorn, reverse proxy, observability, Kafka, admin.

### From system_design_lld_design_patterns_roadmap.md
- **Phase 0:** Programming (Python, OOP, functional basics, memory, exceptions), DSA (arrays, strings, hashmaps, stacks, queues, trees, heaps, graphs, complexity, LRU/LFU).
- **Phase 1:** OOD (SOLID, composition, DI, interfaces, encapsulation), design patterns (Strategy, Factory, Builder, Observer, Decorator, Singleton), API/service design, DB LLD.
- **Phase 2:** Architecture patterns, communication (REST/GraphQL/gRPC, sync/async, queues, Kafka, WebSockets/SSE), data at scale.
- **Phase 3:** Scalability, reliability, security & identity.
- **Phase 4:** Containers/K8s, observability & DevOps.
- **Phase 5:** Advanced patterns (CQRS, event sourcing, Saga, Strangler, API Gateway), distributed systems, engineering judgment.

---

## Tips for Retention

1. **Spaced repetition:** Weeks 11–12 explicitly revisit themes from Weeks 1–10.
2. **Interleaving:** Related topics are mixed (e.g. auth in Python, then FastAPI, then security roadmap).
3. **Explain to retain:** Days 85, 89, and teaching-style tasks force retrieval and clarification.
4. **Checklists:** Use the Topic Coverage Index to tick off items as you go; audit on Days 82–83.
5. **One implementation per concept:** Each day has a concrete “Practice / Retention” suggestion—prefer doing over only reading.

Good luck. By Day 90 you’ll have a structured path from strong foundations to expert-level across both the Skills Checklist and the System Design / LLD / Design Patterns roadmap.
