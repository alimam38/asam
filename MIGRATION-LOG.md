# Migration Log — 2026-06-11

Initial artifact migration into the asam repository. Every file was copied, never moved; all originals remain in place.

**Inventoried:** 1339 files across Dropbox (Claude, Meridia, Meridia_Ingestion/Eden Crown, Eden Crown Systems - Master Architecture), Desktop\Galaxy Zips\EdenCrown, C:\Users\alima\meridia, and keyword-matched files in Downloads and Documents.

**Migrated:** 308 files. **Left behind:** 1031 files (reasons below).

Naming: documents are kebab-case prefixed with their last-modified date (the best available proxy for original date). Code trees keep original filenames so imports and references keep working.

## Migrated

| Source | Destination | Classification | Note |
|---|---|---|---|
| ~\Downloads\AEGIS_JPMC_PARTNERSHIP_DECK.md | assets/aegis/2026-01-26-aegis-jpmc-partnership-deck.md | collateral |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\AWaits Bio.pdf | assets/meridia/2026-01-20-awaits-bio.pdf | collateral | outreach contact bio |
| ~\Dropbox\Meridia\Outreach\Meridia Andre Waits One Pager.pdf | assets/meridia/2026-04-22-meridia-andre-waits-one-pager.pdf | collateral |  |
| ~\Dropbox\Meridia\Outreach\Meridia (BSherman).pdf | assets/meridia/2026-04-22-meridia-bsherman.pdf | collateral |  |
| ~\Dropbox\Meridia\pitch\Meridia Pitch.pdf | assets/meridia/2026-05-23-meridia-pitch.pdf | collateral |  |
| ~\Dropbox\Meridia\Faith Strategies Duncan v1 Professional.docx | assets/meridia/faith-strategies/2026-05-05-faith-strategies-duncan-v1-professional.docx | collateral |  |
| ~\Dropbox\Meridia\Faith Strategies Duncan v1 Professional.pdf | assets/meridia/faith-strategies/2026-05-05-faith-strategies-duncan-v1-professional.pdf | collateral |  |
| ~\Dropbox\Meridia\Faith Strategies Duncan v2 Meridia.docx | assets/meridia/faith-strategies/2026-05-05-faith-strategies-duncan-v2-meridia.docx | collateral |  |
| ~\Dropbox\Meridia\Faith Strategies Duncan v2 Meridia.pdf | assets/meridia/faith-strategies/2026-05-05-faith-strategies-duncan-v2-meridia.pdf | collateral |  |
| ~\Dropbox\Meridia\Faith Strategies Group Geoff Duncan Georgia Governor.docx | assets/meridia/faith-strategies/2026-05-05-faith-strategies-group-geoff-duncan-georgia-governor.docx | collateral |  |
| ~\Dropbox\Meridia\Faith Strategies Group Geoff Duncan Georgia Governor.pdf | assets/meridia/faith-strategies/2026-05-05-faith-strategies-group-geoff-duncan-georgia-governor.pdf | collateral |  |
| ~\Dropbox\Meridia\pitch\Meridia WayPoint OnePager.pdf | assets/waypoint/2026-03-01-meridia-waypoint-onepager.pdf | collateral |  |
| ~\Dropbox\Meridia\files\Meridia_WayPoint_Pitch_Deck.pptx | assets/waypoint/2026-03-01-meridia-waypoint-pitch-deck.pptx | collateral | largest deck export |
| ~\Dropbox\Meridia\files\Meridia_WayPoint_OnePager.html | assets/waypoint/Meridia_WayPoint_OnePager.html | collateral |  |
| ~\Dropbox\Meridia\waypoint_icon_1024.png | assets/waypoint/waypoint_icon_1024.png | collateral |  |
| ~\Downloads\waypoint_sentiarch_flow.png | assets/waypoint/waypoint_sentiarch_flow.png | collateral |  |
| ~\Downloads\waypoint_sentiarch_flow.svg | assets/waypoint/waypoint_sentiarch_flow.svg | collateral |  |
| ~\Downloads\mnt_Aegis-Next-Iteration-Roadmap.md | docs/aegis/2026-01-19-mnt-aegis-next-iteration-roadmap.md | report |  |
| ~\Downloads\mnt_Aegis-System-Assessment.md | docs/aegis/2026-01-19-mnt-aegis-system-assessment.md | report |  |
| ~\Downloads\mnt_Aegis-System-Documentation.md | docs/aegis/2026-01-19-mnt-aegis-system-documentation.md | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\Insights.docx | docs/aegis/2026-01-20-insights.docx | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\CC Recap.docx | docs/aegis/2026-01-21-cc-recap.docx | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\Evaluation Phase Outline.docx | docs/aegis/2026-01-21-evaluation-phase-outline.docx | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\Prior Claude Code.txt | docs/aegis/2026-01-24-prior-claude-code.txt | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\Strategy.docx | docs/aegis/2026-01-24-strategy.docx | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\structure.docx | docs/aegis/2026-01-24-structure.docx | decision record |  |
| ~\Dropbox\Meridia\files\Six Platforms, One Paradigm.pdf | docs/asam/2026-03-02-six-platforms-one-paradigm.pdf | report | umbrella narrative |
| ~\Dropbox\Meridia\Documents\Traverse_Code_Governed_Intelligence_Framework_v1.docx | docs/asam/2026-03-12-traverse-code-governed-intelligence-framework-v1.docx | spec | cross-system governance framework |
| ~\Dropbox\Meridia\Hypomone Eden Reserve\Keena_Cover_Note_v1.md | docs/asam/hypomone/2026-05-28-keena-cover-note-v1.md | spec |  |
| ~\Dropbox\Meridia\Hypomone Eden Reserve\Naming and Architecture v1.md | docs/asam/hypomone/2026-05-28-naming-and-architecture-v1.md | spec |  |
| ~\Dropbox\Meridia\Hypomone Eden Reserve\Naming_and_Architecture_v2.md | docs/asam/hypomone/2026-05-28-naming-and-architecture-v2.md | spec |  |
| ~\Dropbox\Claude\Hypomone\Founding_Member_Survey_Draft_v1.md | docs/asam/hypomone/2026-06-01-founding-member-survey-draft-v1.md | spec | Hypomone: evolution of Waypoint/Aegis/Eden Crown |
| ~\Dropbox\Claude\Hypomone\Market_Read_Addendum_Georgia_Atlanta_v2.md | docs/asam/hypomone/2026-06-01-market-read-addendum-georgia-atlanta-v2.md | spec | Hypomone: evolution of Waypoint/Aegis/Eden Crown |
| ~\Dropbox\Claude\Hypomone\Market_Read_Addendum_Georgia_Atlanta.md | docs/asam/hypomone/2026-06-01-market-read-addendum-georgia-atlanta.md | spec | Hypomone: evolution of Waypoint/Aegis/Eden Crown |
| ~\Dropbox\Claude\Hypomone\Market_Read_v1.md | docs/asam/hypomone/2026-06-01-market-read-v1.md | spec | Hypomone: evolution of Waypoint/Aegis/Eden Crown |
| ~\Dropbox\Claude\Hypomone\Naming_and_Architecture_v1.md | docs/asam/hypomone/2026-06-01-naming-and-architecture-v1.md | spec | Hypomone: evolution of Waypoint/Aegis/Eden Crown |
| ~\Dropbox\Claude\Hypomone\The_Charter_v2.md | docs/asam/hypomone/2026-06-01-the-charter-v2.md | spec | Hypomone: evolution of Waypoint/Aegis/Eden Crown |
| ~\Dropbox\Meridia\legal\Invoice - Meridia Holdings LLC 2026-03-01.pdf | docs/company/2026-03-01-invoice-meridia-holdings-llc-2026-03-01.pdf | decision record |  |
| ~\Dropbox\Meridia\legal\Meridia_Holdings_LLC_Operating_Agreement.docx | docs/company/2026-03-01-meridia-holdings-llc-operating-agreement.docx | decision record |  |
| ~\Dropbox\Meridia\Company Documents\03-11-26 - GA - Formation Document - Meridia Holdings LLC.pdf | docs/company/2026-03-20-03-11-26-ga-formation-document-meridia-holdings-llc.pdf | decision record |  |
| ~\Dropbox\Meridia\Company Documents\Free Basic Operating Agreement - LLC Single Member -- Meridia Holdings LLC.pdf | docs/company/2026-03-20-free-basic-operating-agreement-llc-single-member-meridia-holdings-llc.pdf | decision record |  |
| ~\Dropbox\Meridia\Company Documents\Initial Resolutions - LLC Single Member -- Meridia Holdings LLC.pdf | docs/company/2026-03-20-initial-resolutions-llc-single-member-meridia-holdings-llc.pdf | decision record |  |
| ~\Dropbox\Meridia\legal\Mail - info@meridiallc.com - MX.pdf | docs/company/2026-03-22-mail-infomeridiallc.com-mx.pdf | decision record | mail/MX setup record |
| ~\Dropbox\Meridia\legal\Mail - info@meridiallc.com - Plaid.pdf | docs/company/2026-03-22-mail-infomeridiallc.com-plaid.pdf | decision record |  |
| ~\Dropbox\Meridia\legal\Roundcube Webmail __ Re_ Meridia Holdings LLC __ Plaid Production Request.pdf | docs/company/2026-03-23-roundcube-webmail-re-meridia-holdings-llc-plaid-production-request.pdf | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\System Build Convo (Keith-GPT).docx | docs/eden-crown/2025-11-27-system-build-convo-keith-gpt.docx | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\Research Topics\Galaxy2.docx | docs/eden-crown/research/2026-03-26-galaxy2.docx | report | original research; inferred from corpus location |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude (Son4.5) Review (Rd 1 Second Pass).docx | docs/eden-crown/systemic-review/2026-01-13-claude-son4.5-review-rd-1-second-pass.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude (Son4.5) Review.docx | docs/eden-crown/systemic-review/2026-01-13-claude-son4.5-review.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Gemini (3.0) Review (Rd 1 Second Pass).docx | docs/eden-crown/systemic-review/2026-01-13-gemini-3.0-review-rd-1-second-pass.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Gemini (3.0) Review.docx | docs/eden-crown/systemic-review/2026-01-13-gemini-3.0-review.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Mistral (Large 3 2512) Review (Rd 1 Second Pass).docx | docs/eden-crown/systemic-review/2026-01-13-mistral-large-3-2512-review-rd-1-second-pass.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Mistral (Large 3 2512) Review.docx | docs/eden-crown/systemic-review/2026-01-13-mistral-large-3-2512-review.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Founders Overview (Pure Reflection from GPT 5.1 Thinking).docx | docs/eden-crown/systemic-review/2026-01-16-founders-overview-pure-reflection-from-gpt-5.1-thinking.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Review (1.18.26).docx | docs/eden-crown/systemic-review/2026-01-18-claude-review-1.18.26.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\DeepSeek Review - R1 (0528) - Analysis.docx | docs/eden-crown/systemic-review/2026-01-18-deepseek-review-r1-0528-analysis.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Human Adjudication Memorandum v1.0 (1.18.26).docx | docs/eden-crown/systemic-review/2026-01-18-human-adjudication-memorandum-v1.0-1.18.26.docx | report | adjudication of model reviews |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Internal Insight (Proprietary).docx | docs/eden-crown/systemic-review/2026-01-19-internal-insight-proprietary.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Founder's Overview (Pure Reflection from GPT 5.1 Thinking).pdf | docs/eden-crown/systemic-review/2026-01-20-founders-overview-pure-reflection-from-gpt-5.1-thinking.pdf | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\GPT\Review I.docx | docs/eden-crown/systemic-review/2026-02-05-review-i.docx | report | chunked PDF exports of same content left behind |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\GPT\Review II.docx | docs/eden-crown/systemic-review/2026-02-05-review-ii.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\KSW.pdf | docs/ksw/2026-01-23-ksw.pdf | spec | full KSW document (4.2 MB master export) |
| ~\Dropbox\Meridia\Eleven Labs Grant\pg 2 Grant application.pdf | docs/ksw/2026-04-07-pg-2-grant-application.pdf | decision record | audio-domain grant; KSW inferred |
| ~\Dropbox\Meridia\KSW.docx | docs/ksw/2026-05-24-ksw.docx | spec | newest copy (2026-05-24) |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Meridia_Domain_Strategy.docx | docs/meridia/2026-01-31-meridia-domain-strategy.docx | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Meridia Brand Identity System.docx | docs/meridia/2026-02-02-meridia-brand-identity-system.docx | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Financial_Architecture_Primer.docx | docs/meridia/2026-02-04-financial-architecture-primer.docx | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Reflection.md | docs/meridia/2026-02-06-reflection.md | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Meridia Infrastructure Requirements.docx | docs/meridia/2026-02-07-meridia-infrastructure-requirements.docx | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Meridia_System_Mandate_v1.docx | docs/meridia/2026-02-18-meridia-system-mandate-v1.docx | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Meridia_System_Mandate_v1.md | docs/meridia/2026-02-18-meridia-system-mandate-v1.md | decision record |  |
| ~\Dropbox\Meridia\CLAUDE.md | docs/meridia/2026-02-27-claude-project-instructions.md | decision record | prior project instructions |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\EIG-CAL-2026-001_90-Day_Execution_Calendar.docx | docs/meridia/2026-02-27-eig-cal-2026-001-90-day-execution-calendar.docx | decision record |  |
| ~\Dropbox\Meridia\files\Meridia_Demo_Sprint_Plan.md | docs/meridia/2026-03-01-meridia-demo-sprint-plan.md | decision record |  |
| ~\Dropbox\Meridia\SETUP_CHECKLIST.md | docs/meridia/2026-03-01-setup-checklist.md | decision record |  |
| ~\Dropbox\Meridia\Technical Presentation\Meridia_Technical_Brief_Keith_Mosley.docx | docs/meridia/2026-03-19-meridia-technical-brief-keith-mosley.docx | report |  |
| ~\Dropbox\Meridia\Company Documents\Meridia RD Technical Activities Log.docx | docs/meridia/2026-03-26-meridia-rd-technical-activities-log.docx | decision record |  |
| ~\Dropbox\Meridia\Plaid\Meridia_Plaid_Partnership_Overview.pdf | docs/meridia/2026-03-30-meridia-plaid-partnership-overview.pdf | decision record |  |
| ~\Dropbox\Meridia\Plaid\Meridia_Plaid_Partnership_Overview v3.pdf | docs/meridia/2026-03-31-meridia-plaid-partnership-overview-v3.pdf | decision record |  |
| ~\Dropbox\Meridia\Research\Meridia_Infrastructure_Report.docx | docs/meridia/2026-04-25-meridia-infrastructure-report.docx | report |  |
| ~\Dropbox\Meridia\Company Documents\Meridia_Cathedral_View.docx | docs/meridia/2026-04-28-meridia-cathedral-view.docx | report | newest copy (2026-04-28) |
| ~\Dropbox\Meridia\Company Documents\EIG Meridia Architecture Overview.md | docs/meridia/2026-05-24-eig-meridia-architecture-overview.md | decision record |  |
| ~\Dropbox\Meridia\Company Documents\Meridia Foundation.pdf | docs/meridia/2026-05-24-meridia-foundation.pdf | report |  |
| ~\Dropbox\Meridia\Company Documents\Meridia Review.doc | docs/meridia/2026-05-24-meridia-review.doc | report |  |
| ~\Downloads\integra-core.csv | docs/meridia/reference/2026-03-06-integra-core.csv | report |  |
| ~\Dropbox\Meridia\Documents\Swagger.pdf | docs/meridia/reference/2026-03-06-swagger.pdf | report |  |
| ~\Dropbox\Meridia\FFIEC.zip | docs/meridia/reference/FFIEC.zip | report | small FFIEC data bundle |
| ~\Downloads\Meridian_Signal_Board_Report_1.pdf | docs/meridia/reports/2026-02-22-meridian-signal-board-report-1.pdf | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\MCR-2026-001_Meridian_Continental_Report.docx | docs/meridia/reports/2026-02-27-mcr-2026-001-meridian-continental-report.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\Meridia_Phase1_Assessment.md | docs/meridia/reports/2026-02-27-meridia-phase1-assessment.md | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\Meridian_Signal_Board_Report.pdf | docs/meridia/reports/2026-02-27-meridian-signal-board-report.pdf | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\Meridian_Signal_Family_Report.pdf | docs/meridia/reports/2026-02-27-meridian-signal-family-report.pdf | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\Meridian_Signal_Regulator_Report.pdf | docs/meridia/reports/2026-02-27-meridian-signal-regulator-report.pdf | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\Meridian_Signal_Technical_Report.pdf | docs/meridia/reports/2026-02-27-meridian-signal-technical-report.pdf | report |  |
| ~\Dropbox\Meridia\Meridian_Continental_Volume_I.docx | docs/meridia/reports/2026-03-01-meridian-continental-volume-i.docx | report |  |
| ~\Dropbox\Meridia\Meridia_Cognitive_State_v1.docx | docs/meridia/reports/2026-03-04-meridia-cognitive-state-v1.docx | report |  |
| ~\Dropbox\Meridia\Meridian_Continental_PNFP_Q1_2026.docx | docs/meridia/reports/2026-03-05-meridian-continental-pnfp-q1-2026.docx | report |  |
| ~\Dropbox\Meridia\Meridia_Cognitive_State_v2.docx | docs/meridia/reports/2026-03-06-meridia-cognitive-state-v2.docx | report |  |
| ~\Dropbox\Meridia\Meridian_Continental_PNFP_v2.docx | docs/meridia/reports/2026-03-06-meridian-continental-pnfp-v2.docx | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\compass_artifact_wf-c65bc183-4c56-4848-b77f-f5370c8e8c59_text_markdown.md | docs/meridia/research/2026-02-19-compass-research-1.md | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\compass_artifact_wf-d9ab43db-5775-42b6-9981-7ef580d2f2f0_text_markdown.md | docs/meridia/research/2026-02-19-compass-research-2.md | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Meridia Financial Positioning System_ Multi-Product Fintech Strategy and Competitive Landscape Analysis.pdf | docs/meridia/research/2026-02-19-meridia-financial-positioning-system-multi-product-fintech-strategy-and-competitive-landscape-analysis.pdf | report |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Meridia's International Landscape_ Where Five Products Meet Global Opportunity.pdf | docs/meridia/research/2026-02-19-meridias-international-landscape-where-five-products-meet-global-opportunity.pdf | report |  |
| ~\Dropbox\Meridia\Data Q\Essential Data Feeds for Artificial Intelligence.pdf | docs/meridia/research/2026-03-16-essential-data-feeds-for-artificial-intelligence.pdf | report |  |
| ~\Dropbox\Meridia\Meridiem_Data_Source_Research_Report.docx | docs/meridia/research/2026-03-16-meridiem-data-source-research-report.docx | report |  |
| ~\Dropbox\Meridia\Research\CLAUDE\Claude Repos.docx | docs/process/2026-04-29-claude-repos.docx | decision record |  |
| ~\Dropbox\Meridia\Research\CLAUDE\Claude Design - The Overview.md | docs/process/2026-05-01-claude-design-the-overview.md | decision record |  |
| ~\Dropbox\Claude\Project Instructions.docx | docs/process/2026-05-19-project-instructions.docx | decision record |  |
| ~\Dropbox\Claude\Best_Prompt_Recap_48.md | docs/process/2026-06-10-best-prompt-recap-48.md | decision record |  |
| ~\Dropbox\Claude\Best_Prompt_Recap_F5.md | docs/process/2026-06-10-best-prompt-recap-f5.md | decision record |  |
| ~\Dropbox\Claude\Production Prompts\Cowork Project Instructions.md | docs/process/2026-06-10-cowork-project-instructions.md | decision record | working-method prompt |
| ~\Dropbox\Claude\Production Prompts\Populi Repo Prompt.md | docs/process/2026-06-10-populi-repo-prompt.md | decision record | working-method prompt |
| ~\Dropbox\Claude\Production Prompts\preflight.md | docs/process/2026-06-10-preflight.md | decision record | working-method prompt |
| ~\Dropbox\Claude\Production Prompts\Readiness Report.md | docs/process/2026-06-10-readiness-report.md | decision record | working-method prompt |
| ~\Dropbox\Claude\Production Prompts\repo-scaffold-and-migration prompt.md | docs/process/2026-06-10-repo-scaffold-and-migration-prompt.md | decision record | working-method prompt |
| ~\Dropbox\Meridia\Recess\Reporting\Recess_Intelligence_Brief_Shadow_Rock_Elementary.docx | docs/recess/reports/2026-03-03-recess-intelligence-brief-shadow-rock-elementary.docx | report |  |
| ~\Dropbox\Meridia\Recess\Reporting\Recess_Intelligence_Brief_Shadow_Rock_v2.docx | docs/recess/reports/2026-03-03-recess-intelligence-brief-shadow-rock-v2.docx | report |  |
| ~\Dropbox\Meridia\Recess\Kanetra\shadow_rock_math_gap_analysis_2026.pptx | docs/recess/reports/2026-05-03-shadow-rock-math-gap-analysis-2026.pptx | report |  |
| ~\Dropbox\Meridia\Recess\Kanetra\shadow_rock_assessment_wrap_up_2026.docx | docs/recess/reports/2026-05-04-shadow-rock-assessment-wrap-up-2026.docx | report |  |
| ~\Dropbox\Meridia\Recess\Kanetra\Shadow Rock Elementary · 5th Grade Prerequisite Routing · Spring 2026.pdf | docs/recess/reports/2026-05-04-shadow-rock-elementary-5th-grade-prerequisite-routing-spring-2026.pdf | report | pilot deliverable |
| ~\Dropbox\Meridia\Recess\Kanetra\Shadow Rock Elementary · Math Gap Analysis · Spring 2026.pdf | docs/recess/reports/2026-05-04-shadow-rock-elementary-math-gap-analysis-spring-2026.pdf | report | pilot deliverable |
| ~\Dropbox\Meridia\Recess\Questionnaires\AI-Ready Education Compliance_ A Documentation Automation Blueprint.pdf | docs/recess/research/2026-03-04-ai-ready-education-compliance-a-documentation-automation-blueprint.pdf | report |  |
| ~\Dropbox\Meridia\What_Should_My_Child_Know.html | docs/recess/research/What_Should_My_Child_Know.html | report | Recess-domain content |
| ~\Dropbox\Meridia\files\WayPoint_Demo_Sprint_Plan.md | docs/waypoint/2026-03-01-waypoint-demo-sprint-plan.md | decision record |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\DEPLOY_NAS.md | infra/meridia/DEPLOY_NAS.md | spec | NAS/Docker deployment for integra-core |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\Dockerfile | infra/meridia/Dockerfile | spec | NAS/Docker deployment for integra-core |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\EIG-CORPUS-2026-001_Deployment_Guide.md | infra/meridia/EIG-CORPUS-2026-001_Deployment_Guide.md | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\NAS_DEPLOYMENT.md | infra/meridia/NAS_DEPLOYMENT.md | spec | NAS/Docker deployment for integra-core |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\docker-compose.yml | infra/meridia/docker-compose.yml | spec | NAS/Docker deployment for integra-core |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\env_template.txt | infra/meridia/env_template.txt | spec | NAS/Docker deployment for integra-core |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Introducing Aegis.docx | specs/aegis/2026-01-20-introducing-aegis.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Introducing Aegis.pdf | specs/aegis/2026-01-20-introducing-aegis.pdf | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\AEGIS_COMPLETE_ARCHITECTURE_SESSION_2025-01-25.md | specs/aegis/2026-01-24-aegis-complete-architecture-session-2025-01-25.md | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\Aegis Complete Global Architecture.pdf | specs/aegis/2026-01-24-aegis-complete-global-architecture.pdf | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\AEGIS GLOBAL INSTITUTIONAL INFRASTRUCTURE - Project Instructions v2.0 (claude).docx | specs/aegis/2026-01-24-aegis-global-institutional-infrastructure-project-instructions-v2.0-claude.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\Aegis Prototype - Current Instructions (prepared by Gemini 2.5).docx | specs/aegis/2026-01-24-aegis-prototype-current-instructions-prepared-by-gemini-2.5.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\Aegis_Demo_UseCase_Package.docx | specs/aegis/2026-01-30-aegis-demo-usecase-package.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\Aletheia_Demo_UseCase_Package.docx | specs/aegis/2026-01-30-aletheia-demo-usecase-package.docx | spec |  |
| ~\Downloads\Aegis Complete Global Architecture.docx | specs/aegis/2026-06-01-aegis-complete-global-architecture.docx | spec | newest architecture doc (2026-06-01) |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\EB Final Version.docx | specs/eden-crown/2025-11-27-eb-final-version.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\EB Final Version.pdf | specs/eden-crown/2025-11-27-eb-final-version.pdf | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Sentiarch - Master Brief v3.0 (III).docx | specs/eden-crown/2026-01-07-sentiarch-master-brief-v3.0-iii.docx | spec | latest master brief lineage |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Sentiarch - From Appendix to Full Spec.docx | specs/eden-crown/2026-01-09-sentiarch-from-appendix-to-full-spec.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Sentiarch - Appendix H - Trust, Capital & Reassurance Stack (ECS - NGE).docx | specs/eden-crown/2026-01-12-sentiarch-appendix-h-trust-capital-and-reassurance-stack-ecs-nge.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Sentiarch - Master Brief Outline_Template.docx | specs/eden-crown/2026-01-13-sentiarch-master-brief-outline-template.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Sentiarch - Appendix L -The Manus Layer (Spec).docx | specs/eden-crown/2026-01-18-sentiarch-appendix-l-the-manus-layer-spec.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Appendix H.pdf | specs/eden-crown/2026-01-20-appendix-h.pdf | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Appendix L.pdf | specs/eden-crown/2026-01-20-appendix-l.pdf | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Integrated Concept & Architecture Brief.pdf | specs/eden-crown/2026-01-20-integrated-concept-and-architecture-brief.pdf | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Master Appendix Set.pdf | specs/eden-crown/2026-01-20-master-appendix-set.pdf | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Sentiarch - Master Appendix Set v4 (Full Narrative).docx | specs/eden-crown/2026-01-21-sentiarch-master-appendix-set-v4-full-narrative.docx | spec | latest appendix set lineage |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Sentiarch - Integrated Concept & Architecture Brief (v3).docx | specs/eden-crown/2026-01-24-sentiarch-integrated-concept-and-architecture-brief-v3.docx | spec | latest Sentiarch integrated brief |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Chunk Outputs\Master Architecture - Section 1 & 2.docx | specs/eden-crown/master-architecture/2025-11-23-master-architecture-section-1-and-2.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Chunk Outputs\Master Architecture - Section 3.docx | specs/eden-crown/master-architecture/2025-11-23-master-architecture-section-3.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Chunk Outputs\Master Architecture - Section 4.docx | specs/eden-crown/master-architecture/2025-11-23-master-architecture-section-4.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Chunk Outputs\Master Architecture - Section 5.docx | specs/eden-crown/master-architecture/2025-11-23-master-architecture-section-5.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Chunk Outputs\Master Architecture - Section 6.docx | specs/eden-crown/master-architecture/2025-11-23-master-architecture-section-6.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Chunk Outputs\Master Architecture - Section 7.docx | specs/eden-crown/master-architecture/2025-11-23-master-architecture-section-7.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Chunk Outputs\Master Architecture - Section 8.docx | specs/eden-crown/master-architecture/2025-11-24-master-architecture-section-8.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Chunk Outputs\Master Architecture - Section 9.docx | specs/eden-crown/master-architecture/2025-11-24-master-architecture-section-9.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\EIG-CORPUS-2026-001_AIA_Corpus_Schema.sql | specs/meridia/EIG-CORPUS-2026-001_AIA_Corpus_Schema.sql | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\first_batch_project_files.sql | specs/meridia/first_batch_project_files.sql | spec |  |
| ~\Dropbox\Meridia\Recess\Recess Framework Package 2026.docx | specs/recess/2026-05-24-recess-framework-package-2026.docx | spec |  |
| ~\Dropbox\Meridia\Recess\Questionnaires\Educator_Discovery_Questionnaire (KYN).docx | specs/recess/discovery/2026-03-04-educator-discovery-questionnaire-kyn.docx | spec |  |
| ~\Dropbox\Meridia\Recess\Questionnaires\Recess_Educator_Input_Round2_AP.docx | specs/recess/discovery/2026-03-22-recess-educator-input-round2-ap.docx | spec |  |
| ~\Dropbox\Meridia\Recess\Questionnaires\Recess_Educator_Input_Round2.docx | specs/recess/discovery/2026-03-22-recess-educator-input-round2.docx | spec |  |
| ~\Dropbox\Meridia\Recess\Questionnaires\Recess_Teacher_Brief.docx | specs/recess/discovery/2026-03-22-recess-teacher-brief.docx | spec |  |
| ~\Dropbox\Meridia\Recess\Questionnaires\Recess Part II responses.docx | specs/recess/discovery/2026-03-25-recess-part-ii-responses.docx | spec |  |
| ~\Downloads\Sentiarch_WayPoint_Brief_v1.docx | specs/waypoint/2025-12-23-sentiarch-waypoint-brief-v1.docx | spec |  |
| ~\Downloads\Sentiarch_WayPoint_visual_spec_draft_v1.pptx | specs/waypoint/2025-12-26-sentiarch-waypoint-visual-spec-draft-v1.pptx | spec |  |
| ~\Downloads\Waypoint_Sanitized_Spec_Cover_Note_v1.docx | specs/waypoint/2026-01-02-waypoint-sanitized-spec-cover-note-v1.docx | spec |  |
| ~\Downloads\Waypoint_Sentiarch_Appendix_Tech_Spine_v1.docx | specs/waypoint/2026-01-02-waypoint-sentiarch-appendix-tech-spine-v1.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Sentiarch - Appendix D - WayPoint FPS & Product Tiers.docx | specs/waypoint/2026-01-13-sentiarch-appendix-d-waypoint-fps-and-product-tiers.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Appendix D.pdf | specs/waypoint/2026-01-20-appendix-d.pdf | spec | WayPoint FPS & product tiers |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Appendix K.pdf | specs/waypoint/2026-01-20-appendix-k.pdf | spec | WayPoint Renaissance & Edge |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\02_Architecture\Executive Brief\Spec Versions\Sentiarch - Appendix K - WayPoint Renaissance & Edge.docx | specs/waypoint/2026-01-20-sentiarch-appendix-k-waypoint-renaissance-and-edge.docx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\START_AEGIS.bat | src/aegis/START_AEGIS.bat | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\aegis-backend\QUICKREF.md | src/aegis/aegis-backend/QUICKREF.md | spec | Aegis backend prototype |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\aegis-backend\README.md | src/aegis/aegis-backend/README.md | spec | Aegis backend prototype |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\aegis-backend\SETUP_GUIDE.md | src/aegis/aegis-backend/SETUP_GUIDE.md | spec | Aegis backend prototype |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\aegis-backend\api_v1.py | src/aegis/aegis-backend/api_v1.py | spec | Aegis backend prototype |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\aegis-backend\data_generator.py | src/aegis/aegis-backend/data_generator.py | spec | Aegis backend prototype |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\aegis-backend\main.py | src/aegis/aegis-backend/main.py | spec | Aegis backend prototype |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\aegis-backend\models.py | src/aegis/aegis-backend/models.py | spec | Aegis backend prototype |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\aegis-backend\requirements.txt | src/aegis/aegis-backend/requirements.txt | spec | Aegis backend prototype |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\Index.html | src/aegis/prototypes/Index.html | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\Index2.html | src/aegis/prototypes/Index2.html | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Aegis)\Index8.html | src/aegis/prototypes/Index8.html | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\index3.html | src/aegis/prototypes/index3.html | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\index4.html | src/aegis/prototypes/index4.html | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Code\index5.html | src/aegis/prototypes/index5.html | spec |  |
| ~\Dropbox\Meridia\Kingdom Soundworks\circle_of_fifths.jsx | src/ksw/circle_of_fifths.jsx | spec |  |
| ~\Dropbox\Meridia\integra-core\CLAUDE.md | src/meridia/integra-core/CLAUDE.md | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\Index8-live.html | src/meridia/integra-core/Index8-live.html | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\README.md | src/meridia/integra-core/README.md | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\WIRING_GUIDE.md | src/meridia/integra-core/WIRING_GUIDE.md | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\add_endpoints.py | src/meridia/integra-core/add_endpoints.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\alter_census.py | src/meridia/integra-core/alter_census.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\__init__.py | src/meridia/integra-core/app/__init__.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\aletheia_engine.py | src/meridia/integra-core/app/aletheia_engine.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\main.py | src/meridia/integra-core/app/main.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\mock_data.py | src/meridia/integra-core/app/mock_data.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\models.py | src/meridia/integra-core/app/models.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\routers\__init__.py | src/meridia/integra-core/app/routers/__init__.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\routers\aletheia.py | src/meridia/integra-core/app/routers/aletheia.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\routers\entities.py | src/meridia/integra-core/app/routers/entities.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\routers\governance.py | src/meridia/integra-core/app/routers/governance.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\routers\position.py | src/meridia/integra-core/app/routers/position.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\routers\reports.py | src/meridia/integra-core/app/routers/reports.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\routers\scenario.py | src/meridia/integra-core/app/routers/scenario.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\routers\signals.py | src/meridia/integra-core/app/routers/signals.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\services\__init__.py | src/meridia/integra-core/app/services/__init__.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\services\report_generator.py | src/meridia/integra-core/app/services/report_generator.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\services\scenario_engine.py | src/meridia/integra-core/app/services/scenario_engine.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\app\services\trust_index.py | src/meridia/integra-core/app/services/trust_index.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\check_tables.py | src/meridia/integra-core/check_tables.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\cra_map.html | src/meridia/integra-core/cra_map.html | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\alfred\alfred_CPIAUCSL.csv | src/meridia/integra-core/data/alfred/alfred_CPIAUCSL.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\alfred\alfred_FEDFUNDS.csv | src/meridia/integra-core/data/alfred/alfred_FEDFUNDS.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\alfred\alfred_GANGSP.csv | src/meridia/integra-core/data/alfred/alfred_GANGSP.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\alfred\alfred_GAUR.csv | src/meridia/integra-core/data/alfred/alfred_GAUR.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\census\atlanta_msa_census_tracts.csv | src/meridia/integra-core/data/census/atlanta_msa_census_tracts.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fdic\georgia_sod.csv | src/meridia/integra-core/data/fdic/georgia_sod.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\ATLA013URN.csv | src/meridia/integra-core/data/fred/ATLA013URN.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\ATNHPIUS12060Q.csv | src/meridia/integra-core/data/fred/ATNHPIUS12060Q.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\CPIAUCSL.csv | src/meridia/integra-core/data/fred/CPIAUCSL.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\DGS10.csv | src/meridia/integra-core/data/fred/DGS10.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\DPRIME.csv | src/meridia/integra-core/data/fred/DPRIME.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\FEDFUNDS.csv | src/meridia/integra-core/data/fred/FEDFUNDS.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\GABPPRIVSA.csv | src/meridia/integra-core/data/fred/GABPPRIVSA.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\GANGSP.csv | src/meridia/integra-core/data/fred/GANGSP.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\GAPOP.csv | src/meridia/integra-core/data/fred/GAPOP.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\GAUR.csv | src/meridia/integra-core/data/fred/GAUR.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\fred\MORTGAGE30US.csv | src/meridia/integra-core/data/fred/MORTGAGE30US.csv | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\geofred\county_shapes.geojson | src/meridia/integra-core/data/geofred/county_shapes.geojson | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\geofred\msa_shapes.geojson | src/meridia/integra-core/data/geofred/msa_shapes.geojson | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\geofred\state_shapes.geojson | src/meridia/integra-core/data/geofred/state_shapes.geojson | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\data\manifest.json | src/meridia/integra-core/data/manifest.json | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\deploy_financial_schema.py | src/meridia/integra-core/deploy_financial_schema.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\deploy_schema.py | src/meridia/integra-core/deploy_schema.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\fix_census_table.py | src/meridia/integra-core/fix_census_table.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\fix_plaid.py | src/meridia/integra-core/fix_plaid.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\fix_unicode.py | src/meridia/integra-core/fix_unicode.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\fred_data_pull.py | src/meridia/integra-core/fred_data_pull.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\integra-wiring.js | src/meridia/integra-core/integra-wiring.js | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\load_all_data.py | src/meridia/integra-core/load_all_data.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\load_ffiec.py | src/meridia/integra-core/load_ffiec.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\load_ffiec_2024.py | src/meridia/integra-core/load_ffiec_2024.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\load_tract_centroids.py | src/meridia/integra-core/load_tract_centroids.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\mcp_corpus_receiver.py | src/meridia/integra-core/mcp_corpus_receiver.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\README.md | src/meridia/integra-core/meridia-wiring/README.md | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\aletheia_engine.py | src/meridia/integra-core/meridia-wiring/aletheia_engine.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\config.py | src/meridia/integra-core/meridia-wiring/config.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\crud.py | src/meridia/integra-core/meridia-wiring/crud.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\database.py | src/meridia/integra-core/meridia-wiring/database.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\feeds\pull_all.py | src/meridia/integra-core/meridia-wiring/feeds/pull_all.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\main.py | src/meridia/integra-core/meridia-wiring/main.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\models.py | src/meridia/integra-core/meridia-wiring/models.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\mx_adapter.py | src/meridia/integra-core/meridia-wiring/mx_adapter.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\requirements.txt | src/meridia/integra-core/meridia-wiring/requirements.txt | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\scheduler.py | src/meridia/integra-core/meridia-wiring/scheduler.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\schema.sql | src/meridia/integra-core/meridia-wiring/schema.sql | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia-wiring\setup.sh | src/meridia/integra-core/meridia-wiring/setup.sh | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\meridia_cognitive_seed.sql | src/meridia/integra-core/meridia_cognitive_seed.sql | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\pull_hmda_final.py | src/meridia/integra-core/pull_hmda_final.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\pull_hmda_fixed.py | src/meridia/integra-core/pull_hmda_fixed.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\pull_hmda_v3.py | src/meridia/integra-core/pull_hmda_v3.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\requirements.txt | src/meridia/integra-core/requirements.txt | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\seed_entities.py | src/meridia/integra-core/seed_entities.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\test_plaid.py | src/meridia/integra-core/test_plaid.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\test_plaid2.py | src/meridia/integra-core/test_plaid2.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\update_config.py | src/meridia/integra-core/update_config.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\update_creds.py | src/meridia/integra-core/update_creds.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\wire_index8.py | src/meridia/integra-core/wire_index8.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\wire_index8_final.py | src/meridia/integra-core/wire_index8_final.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\Dropbox\Meridia\integra-core\wire_index8_live.py | src/meridia/integra-core/wire_index8_live.py | spec | canonical Meridia codebase (newest, active through 2026-05) |
| ~\meridia\integra-wiring\README.md | src/meridia/integra-wiring/README.md | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\_query_hmda.py | src/meridia/integra-wiring/_query_hmda.py | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\_resolve_leis.py | src/meridia/integra-wiring/_resolve_leis.py | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\config.py | src/meridia/integra-wiring/config.py | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\crud.py | src/meridia/integra-wiring/crud.py | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\database.py | src/meridia/integra-wiring/database.py | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\feeds\pull_all.py | src/meridia/integra-wiring/feeds/pull_all.py | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\main.py | src/meridia/integra-wiring/main.py | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\models.py | src/meridia/integra-wiring/models.py | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\mx_adapter.py | src/meridia/integra-wiring/mx_adapter.py | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\requirements.txt | src/meridia/integra-wiring/requirements.txt | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\scheduler.py | src/meridia/integra-wiring/scheduler.py | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\schema.sql | src/meridia/integra-wiring/schema.sql | spec | local working copy; differs from integra-core meridia-wiring |
| ~\meridia\integra-wiring\setup.sh | src/meridia/integra-wiring/setup.sh | spec | local working copy; differs from integra-core meridia-wiring |
| ~\Dropbox\Meridia\prototypes\Index8.html | src/meridia/prototypes/Index8.html | spec | later variant (2026-04-03) |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\Index8_wired.html | src/meridia/prototypes/Index8_wired.html | spec |  |
| ~\Downloads\Meridia_Texas_CRA_Andre.html | src/meridia/prototypes/Meridia_Texas_CRA_Andre.html | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\meridia-arrival.jsx | src/meridia/prototypes/meridia-arrival.jsx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\meridia-cathedral.jsx | src/meridia/prototypes/meridia-cathedral.jsx | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\meridia-v3.jsx | src/meridia/prototypes/meridia-v3.jsx | spec |  |
| ~\Dropbox\Meridia\Technical Presentation\meridia_architecture.html | src/meridia/prototypes/meridia_architecture.html | spec |  |
| ~\Downloads\meridia_iamp_v2.html | src/meridia/prototypes/meridia_iamp_v2.html | spec |  |
| ~\Downloads\meridia_stress_test.html | src/meridia/prototypes/meridia_stress_test.html | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\aia_cataloger.py | src/meridia/services/aia_cataloger.py | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Artifacts\aletheia_service.py | src/meridia/services/aletheia_service.py | spec |  |
| ~\Dropbox\Meridia\Recess\Prototypes\Recess_Ethan_Demo.html | src/recess/prototypes/Recess_Ethan_Demo.html | spec |  |
| ~\Dropbox\Meridia\Recess\Prototypes\Recess_Ethan_Demo_v2.html | src/recess/prototypes/Recess_Ethan_Demo_v2.html | spec |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\South_Atlanta_District_Redesign.html | src/recess/prototypes/South_Atlanta_District_Redesign.html | spec | Recess-domain artifact |
| ~\Dropbox\Meridia\Recess\Prototypes\recess_prototype.html | src/recess/prototypes/recess_prototype.html | spec |  |
| ~\Dropbox\Meridia\Hypomone Eden Reserve\System Files\PY\run_fps.py | src/waypoint/fps/run_fps.py | spec | FPS script from Hypomone; WayPoint owns FPS per Appendix D |
| ~\Downloads\waypoint_adaptive.html | src/waypoint/prototypes/waypoint_adaptive.html | spec |  |
| ~\Downloads\waypoint_adaptive_1.html | src/waypoint/prototypes/waypoint_adaptive_1.html | spec |  |

## Left behind

- **Dropbox\Meridia\Taxes\* (505 files)** — Personal tax-software data (TurboTax .dat/.ta*/.dll), not product artifacts.
- **Dropbox\Meridia\integra-core - Copy\*, meridia_wiring_package - Copy\*, Data Q - Copy\*, corpus - Copy\*, prototypes - Copy\* (127 files)** — Windows "- Copy" duplicate folders; canonical copies migrated or assessed.
- **Dropbox\Meridia\files\* (42 remaining files)** — March 1 snapshot: code superseded by src/meridia/integra-core (same modules, newer); Turner/TTS client deliverables out of product scope; remaining docs are duplicates of migrated copies.
- **Dropbox\Meridia\meridia_wiring_package\* + .zip (12 files)** — Superseded by the newer meridia-wiring inside src/meridia/integra-core.
- **Dropbox\Meridia\integra-core excluded items (28 files)** — .env (secrets — never committed), .claude settings, __pycache__ bytecode, and nested duplicate copies of Data Q and Kingdom Soundworks files migrated from their top-level locations.
- **Dropbox\Meridia\Data Q\API Data Keys.docx (+ conflicted copy)** — Contains live API credentials. Secrets are never committed. Move keys to a password manager / .env on the NAS; the question to close: which keys are still active?
- **Downloads\Meridia_Core_volume1.rkey** — Key material — never committed.
- **Desktop\Galaxy Zips\EdenCrown\EdenCrown1-11.zip (11 archives, ~450 MB)** — Phone-export archives; too large for git history. FOLLOW-UP: extract, classify contents, migrate keepers in a second pass.
- **Meridia_Ingestion\...\RelayFi (Model)\* (32 files) and Banking Options\* (4 files)** — Competitor/bank web-page captures; reference material, not original work. Keep in Dropbox.
- **Meridia_Ingestion\...\Research Topics\* (50 remaining files)** — Web clippings (TechCrunch, Reuters, vendor pages); Galaxy2.docx (original work) was migrated.
- **Meridia_Ingestion\...\GPT\Review 1*.pdf and Review II.pdf (19 files, ~90 MB)** — Chunked/whole PDF exports of the same content as the migrated Review I.docx and Review II.docx.
- **Meridia_Ingestion\...\Executive Brief superseded versions (~16 files)** — Earlier versions in lineages where the latest was migrated (EB v1/v2 + .pages, Sentiarch v2/v2.1/v3-narrative/stitched/copy variants).
- **Meridia_Ingestion\...\System Builds\*, 00_System_Optimization\* (8 files)** — PC hardware procurement docs, not product artifacts.
- **Meridia_Ingestion\...\Year in Review (PWS)\* (19 files)** — Personal ChatGPT year-in-review images.
- **Meridia_Ingestion\...\Claude Project (Meridia): zips, nested integra-core copies, clippings (~45 files)** — Zip archives whose extracted contents were assessed; Feb 19/22/27 integra-core copies superseded by the canonical Dropbox\Meridia\integra-core; research clippings (Claude 4.6.pdf, Poe pricing, memory-architecture PDFs); TTS/Turner client letters and templates.
- **Meridia_Ingestion\...\Claude Code: news PDFs, filesv3.zip, dup exports (~10 files)** — Web clippings (Brave, Reuters, TechCrunch, AVERI), zip of files migrated individually, .instructions.txt/.html.docx duplicate exports.
- **Meridia_Ingestion\...\Claude Code\Document (10).docx** — AMBIGUOUS — unidentifiable name. Question to close: what is this document? Review and re-file manually.
- **Meridia_Ingestion\...\Personal\, Bank of the Future.pdf, the-bank-of-the-future.htm, AuthForm** — Personal records and article captures.
- **Dropbox\Eden Crown Systems - Master Architecture\...\My-Bill-03.08.2026 conv.docx** — Personal billing conversation, not a product artifact.
- **Dropbox\Claude: .env, SKILL folders (4 files), Claude Workspace (6 files), preflight.md (root), tts_authnet_reporting.py** — .env is secret; skills are Claude tooling that lives in the skills system; Claude Workspace is an Obsidian vault shell (.obsidian excluded by convention); root preflight.md duplicates the Production Prompts copy; tts script is Turner client work.
- **Downloads duplicates (12 files)** — Byte-or-version duplicates of migrated files: MCR report, invoice, Recess briefs/demo, Cathedral View, meridia_architecture.html, AEGIS session .md, smaller START_AEGIS.bat, WayPoint one-pager/deck, Signal reports.
- **Downloads\Nexus-Eden Crown credit usage .csv** — Platform billing record, not a product artifact.
- **Downloads\Lilly Foundation\* and X64W11...\* (4 files)** — Client grant work (Turner) and Intel driver files matched by keyword noise.
- **Documents\PDF X\* (5 files)** — Smaller/alternate exports (conv.txt conversions, compressed KSW.pdf) of documents migrated from their primary locations.
- **Dropbox\Meridia\Company Documents: resume, photo .png, webmail .pdf, downloaded_documents.zip** — Personal resume, raw image, mail screenshot, and an unsorted download bundle — not product artifacts.
- **Dropbox\Meridia\Recess\Kanetra: 2 resumes, retest .xlsx, SRE testing packet** — Third-party personal documents and raw student testing records; the derived Recess deliverables were migrated.
- **Dropbox\Meridia root: DISC-A Neal.pdf, IMG_5838*, Screenshot*.pdf, Gammon report, Turner audit, upwork.pdf, files.zip, AI-Ready...pdf (root dup), Research\*.url, pitch dups (2)** — Personal assessment, photos, screenshots, client (Gammon/Turner) deliverables, marketplace page capture, zip of migrated folder, duplicate copies.
- **C:\Users\alima\meridia\integra-wiring excluded (7 files)** — .env (secrets), .claude settings, __pycache__ bytecode.
- **Artifacts still in the Claude platform** — NOT ON DISK — noted from interview. FOLLOW-UP: export remaining artifacts from Claude.ai conversations to a folder, then run a second migration pass.

## Standing rules applied

- Secrets (.env, API key documents, .rkey) are never committed, anywhere, ever.
- Originals were never moved or deleted; everything was copied.
- Where multiple versions existed, the newest/most complete copy was migrated and earlier versions were left with their lineage noted.

## Second pass — Turner (client engagement), 2026-06-11

Turner Theological Seminary is a client engagement / proving ground for ASAM systems. Engagement **work products** (deliverables Aliman produced for Turner) were migrated to `docs/clients/turner/`; the seminary's **institutional records** were deliberately left in Dropbox.

**Inventoried:** ~4,447 Turner-related files. **Migrated:** 86. **Left behind:** ~4,360.

### Migrated

| Source | Destination | Classification | Note |
|---|---|---|---|
| ~\Dropbox\Meridia\files\COWORK_TURNER_INSTRUCTIONS.md | docs/clients/turner/2026-03-01-cowork-turner-instructions.md | decision record |  |
| ~\Dropbox\Meridia\files\TURNER_COWORK_INSTRUCTIONS.md | docs/clients/turner/2026-03-01-turner-cowork-instructions.md | decision record |  |
| ~\Downloads\Capital Campaign - Phase III (1)\uploads\Turner Brand Guide.pdf | docs/clients/turner/brand/2026-05-16-turner-brand-guide.pdf | collateral | pptx source left in Dropbox |
| ~\Dropbox\Turner\President Reports\Phase III\Prior Designs\TTS_Case_for_Support_Phase_III.docx | docs/clients/turner/capital-campaign-phase-iii/2026-05-07-tts-case-for-support-phase-iii.docx | collateral | source doc |
| ~\Dropbox\Turner\President Reports\Phase III\Prior Designs\TTS_Gift_Opportunity_Summary.docx | docs/clients/turner/capital-campaign-phase-iii/2026-05-07-tts-gift-opportunity-summary.docx | collateral | source doc |
| ~\Dropbox\Turner\President Reports\Phase III\Prior Designs\TTS_Phase_III_Capital_Campaign_Proforma (B).docx | docs/clients/turner/capital-campaign-phase-iii/2026-05-07-tts-phase-iii-capital-campaign-proforma-b.docx | collateral | source doc |
| ~\Dropbox\Turner\President Reports\Phase III\Prior Designs\TTS_Phase_III_Capital_Campaign_Proforma.docx | docs/clients/turner/capital-campaign-phase-iii/2026-05-07-tts-phase-iii-capital-campaign-proforma.docx | collateral | source doc |
| ~\Dropbox\Turner\President Reports\Phase III\Final Revisions\TTS Phase III — Capital Campaign (Full Detail) v4.pdf | docs/clients/turner/capital-campaign-phase-iii/2026-05-14-tts-phase-iii-capital-campaign-full-detail-v4.pdf | collateral | latest revision; v2/v3 left in Dropbox |
| ~\Dropbox\Turner\President Reports\Phase III\Current Designs\TTS Phase III - Capital Campaign (Full Detail).pdf | docs/clients/turner/capital-campaign-phase-iii/2026-05-14-tts-phase-iii-capital-campaign-full-detail.pdf | collateral |  |
| ~\Dropbox\Turner\President Reports\Phase III\Current Designs\TTS Phase III - Capital Campaign Proforma v3.pdf | docs/clients/turner/capital-campaign-phase-iii/2026-05-14-tts-phase-iii-capital-campaign-proforma-v3.pdf | collateral |  |
| ~\Downloads\Capital Campaign - Phase III (1)\uploads\TTS_5Year_Budget_FY2026_2031 (Updated 2).xlsx | docs/clients/turner/capital-campaign-phase-iii/2026-05-16-tts-5year-budget-fy2026-2031-updated-2.xlsx | report |  |
| ~\Dropbox\Turner\President Reports\Phase III\Html Designs\tts-redesign-print.html | docs/clients/turner/capital-campaign-phase-iii/html/tts-redesign-print.html | collateral |  |
| ~\Dropbox\Turner\President Reports\Phase III\Html Designs\tts-redesign.html | docs/clients/turner/capital-campaign-phase-iii/html/tts-redesign.html | collateral |  |
| ~\Dropbox\Turner\President Reports\Phase III\Html Designs\tts-system.html | docs/clients/turner/capital-campaign-phase-iii/html/tts-system.html | collateral |  |
| ~\Downloads\2024 Turner FARF.xlsx | docs/clients/turner/financial-analysis/2025-12-18-2024-turner-farf.xlsx | report |  |
| ~\Downloads\net asset rollforward Turner.xlsx | docs/clients/turner/financial-analysis/2026-01-25-net-asset-rollforward-turner.xlsx | report |  |
| ~\Downloads\R-14 2025 Turner Composite Score - CLIENT.pdf | docs/clients/turner/financial-analysis/2026-03-17-r-14-2025-turner-composite-score-client.pdf | report |  |
| ~\Downloads\R-14 2025 Turner Composite Score - CLIENT.xlsx | docs/clients/turner/financial-analysis/2026-03-17-r-14-2025-turner-composite-score-client.xlsx | report |  |
| ~\Downloads\R-14 Composite Score Calculation - Turner 2024 Audit (F).xlsx | docs/clients/turner/financial-analysis/2026-03-17-r-14-composite-score-calculation-turner-2024-audit-f.xlsx | report |  |
| ~\Downloads\'Turner Composite Financial Index calculator.xls | docs/clients/turner/financial-analysis/2026-04-20-turner-composite-financial-index-calculator.xls | report |  |
| ~\Downloads\2025 Audit Report - Turner Theological Financials (F).pdf | docs/clients/turner/financial-analysis/2026-05-18-2025-audit-report-turner-theological-financials-f.pdf | report | final audited financials deliverable |
| ~\Downloads\TTS 2025 - 2026 Operating Budget.pdf | docs/clients/turner/financial-analysis/2026-05-18-tts-2025-2026-operating-budget.pdf | report |  |
| ~\Dropbox\Turner\Grants\GA EMS\GA FPC\Turner_FPC_Investment_Justification_2026.docx | docs/clients/turner/grants/ga-fpc-2026/2026-05-19-turner-fpc-investment-justification-2026.docx | collateral |  |
| ~\Dropbox\Turner\Grants\GA EMS\GA FPC\Attachment-E-Certifications-Lobbying--Debarment--Suspension-(executed).pdf | docs/clients/turner/grants/ga-fpc-2026/2026-05-22-attachment-e-certifications-lobbying-debarment-suspension-executed.pdf | collateral |  |
| ~\Dropbox\Turner\Grants\GA EMS\GA FPC\SCRFormVersion5 (Executed).pdf | docs/clients/turner/grants/ga-fpc-2026/2026-05-22-scrformversion5-executed.pdf | collateral |  |
| ~\Dropbox\Turner\Grants\GA EMS\GA FPC\FY2026_Georgia_Funds_for_Protected_Communities_Grant_Program_Application.pdf | docs/clients/turner/grants/ga-fpc-2026/2026-05-26-fy2026-georgia-funds-for-protected-communities-grant-program-application.pdf | collateral |  |
| ~\Dropbox\Turner\Grants\GA EMS\2025 NSGP\(CISA)_Houses_of_Worship_-_Turner_Seminary.pdf | docs/clients/turner/grants/nsgp-2025/2026-05-18-cisa-houses-of-worship-turner-seminary.pdf | collateral |  |
| ~\Dropbox\Turner\Grants\GA EMS\2025 NSGP\FY2025-NSGP-Vulnerability_Assessment_-_Turner.pdf | docs/clients/turner/grants/nsgp-2025/2026-05-18-fy2025-nsgp-vulnerability-assessment-turner.pdf | collateral |  |
| ~\Dropbox\Turner\Grants\GA EMS\2025 NSGP\FY_2025_NSGP_Investment-Justification-118451-48287.docx | docs/clients/turner/grants/nsgp-2025/2026-05-19-fy-2025-nsgp-investment-justification-118451-48287.docx | collateral |  |
| ~\Dropbox\Turner\Grants\GA EMS\2025 NSGP\FY_2025_NSGP_Investment-Justification-118451-48287.pdf | docs/clients/turner/grants/nsgp-2025/2026-05-19-fy-2025-nsgp-investment-justification-118451-48287.pdf | collateral |  |
| ~\Dropbox\Turner\Grants\GA EMS\2025 NSGP\FY2025 Nonprofit Security Grant - Turner's Supplemental Information for Application.pdf | docs/clients/turner/grants/nsgp-2025/2026-05-19-fy2025-nonprofit-security-grant-turners-supplemental-information-for-application.pdf | collateral |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\TTS_Donation_Letter_Template.docx | docs/clients/turner/letters/2026-02-16-tts-donation-letter-template.docx | collateral |  |
| ~\Dropbox\Meridia\files\TSF_Letter_of_Intent_Fillable.pdf | docs/clients/turner/letters/2026-03-01-tsf-letter-of-intent-fillable.pdf | collateral |  |
| ~\Dropbox\Meridia\files\TTS_Student_Account_Letter.docx | docs/clients/turner/letters/2026-03-01-tts-student-account-letter.docx | collateral |  |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Education Templates.zip | docs/clients/turner/letters/Education Templates.zip | collateral | template bundle |
| ~\Dropbox\Meridia_Ingestion\Eden Crown Systems - Master Architecture\03_Systemic Review\Claude Project (Meridia)\Letters.zip | docs/clients/turner/letters/Letters.zip | collateral | letter template bundle |
| ~\Dropbox\Turner\Lilly\Lilly Endowment Team.docx | docs/clients/turner/lilly/2026-05-16-lilly-endowment-team.docx | collateral |  |
| ~\Dropbox\Turner\Lilly\Lilly Endowment Team.pdf | docs/clients/turner/lilly/2026-05-16-lilly-endowment-team.pdf | collateral |  |
| ~\Downloads\Lilly Foundation\Lilly Foundation\Narrative Draft\Lilly Grant Proposal - The Turner Model - Integrated Christian Practices Initiative.docx | docs/clients/turner/lilly/2026-05-16-lilly-grant-proposal-the-turner-model-integrated-christian-practices-initiative.docx | collateral |  |
| ~\Dropbox\Turner\Lilly\The Budget Philosophy.docx | docs/clients/turner/lilly/2026-05-16-the-budget-philosophy.docx | collateral |  |
| ~\Dropbox\Turner\Lilly\Turner_Lilly_Budget_2026.xlsx | docs/clients/turner/lilly/2026-05-16-turner-lilly-budget-2026.xlsx | collateral |  |
| ~\Dropbox\Turner\Lilly\Turner_Lilly_Budget_Narrative_2026.docx | docs/clients/turner/lilly/2026-05-16-turner-lilly-budget-narrative-2026.docx | collateral |  |
| ~\Dropbox\Turner\Lilly\Official Request Letter - Lilly Endowment Grant.docx | docs/clients/turner/lilly/2026-05-17-official-request-letter-lilly-endowment-grant.docx | collateral |  |
| ~\Dropbox\Turner\Lilly\Official Request Letter - Lilly Endowment Grant.pdf | docs/clients/turner/lilly/2026-05-17-official-request-letter-lilly-endowment-grant.pdf | collateral |  |
| ~\Downloads\Budget Narrative - The Turner Model.xlsx - Budget Narrative.pdf | docs/clients/turner/lilly/2026-05-18-budget-narrative-the-turner-model.xlsx-budget-narrative.pdf | collateral |  |
| ~\Downloads\Information Form - Turner Theological Seminary (1).pdf | docs/clients/turner/lilly/2026-05-18-information-form-turner-theological-seminary-1.pdf | collateral |  |
| ~\Downloads\Line Item Budget - The Turner Model.xlsx - Line-Item Budget.pdf | docs/clients/turner/lilly/2026-05-18-line-item-budget-the-turner-model.xlsx-line-item-budget.pdf | collateral |  |
| ~\Downloads\Summary Budget - The Turner Model.xlsx - Summary Budget.pdf | docs/clients/turner/lilly/2026-05-18-summary-budget-the-turner-model.xlsx-summary-budget.pdf | collateral |  |
| ~\Downloads\The Turner Model - Budget Summary.xlsx | docs/clients/turner/lilly/2026-05-18-the-turner-model-budget-summary.xlsx | collateral |  |
| ~\Downloads\Lilly Endowment RFP - Exploring Christian Practices Initiative (1)\Revised Budget Package\Turner_Lilly_Budget_2026_OPTION1.xlsx | docs/clients/turner/lilly/revised-budget-package/2026-05-16-turner-lilly-budget-2026-option1.xlsx | collateral |  |
| ~\Downloads\Lilly Endowment RFP - Exploring Christian Practices Initiative (1)\Revised Budget Package\Turner_Lilly_Budget_2026_REVISED.xlsx | docs/clients/turner/lilly/revised-budget-package/2026-05-16-turner-lilly-budget-2026-revised.xlsx | collateral |  |
| ~\Downloads\Lilly Endowment RFP - Exploring Christian Practices Initiative (1)\Revised Budget Package\Turner_Lilly_Budget_Narrative_2026_REVISED.docx | docs/clients/turner/lilly/revised-budget-package/2026-05-16-turner-lilly-budget-narrative-2026-revised.docx | collateral |  |
| ~\Downloads\Lilly Endowment RFP - Exploring Christian Practices Initiative (1)\Revised Budget Package\Turner_Lilly_Budget_Narrative_OPTION1.docx | docs/clients/turner/lilly/revised-budget-package/2026-05-16-turner-lilly-budget-narrative-option1.docx | collateral |  |
| ~\Downloads\Lilly Endowment RFP - Exploring Christian Practices Initiative (1)\Revised Budget Package\Turner_Lilly_Submission_Index.html | docs/clients/turner/lilly/revised-budget-package/2026-05-16-turner-lilly-submission-index.html | collateral |  |
| ~\Downloads\Lilly Endowment RFP - Exploring Christian Practices Initiative (1)\Revised Budget Package\Turner_Lilly_Summary_Budget_Onepage.html | docs/clients/turner/lilly/revised-budget-package/2026-05-16-turner-lilly-summary-budget-onepage.html | collateral |  |
| ~\Downloads\Lilly Endowment RFP - Exploring Christian Practices Initiative (1)\Revised Budget Package\Turner_Lilly_What_Changed_OPTION1.docx | docs/clients/turner/lilly/revised-budget-package/2026-05-16-turner-lilly-what-changed-option1.docx | collateral |  |
| ~\Downloads\Lilly Endowment RFP - Exploring Christian Practices Initiative (1)\Revised Budget Package\Turner_Proposal_Narrative_Outline.docx | docs/clients/turner/lilly/revised-budget-package/2026-05-16-turner-proposal-narrative-outline.docx | collateral |  |
| ~\Downloads\Lilly Endowment RFP - Exploring Christian Practices Initiative (1)\Revised Budget Package\Budget Revisions Suggestions\Turner_Rebuilt_Budget_Formatted.xlsx | docs/clients/turner/lilly/revised-budget-package/2026-05-16-turner-rebuilt-budget-formatted.xlsx | collateral |  |
| ~\Downloads\Lilly Endowment RFP - Exploring Christian Practices Initiative (1)\Revised Budget Package\Budget Revisions Suggestions\Turner_Revised_Budget_Narrative.docx | docs/clients/turner/lilly/revised-budget-package/2026-05-16-turner-revised-budget-narrative.docx | collateral |  |
| ~\Downloads\Turner_Lilly_Submission_Package\Option 1\Option_1_Summary_Budget_standalone.html | docs/clients/turner/lilly/submission-package/option-1/2026-05-16-option-1-summary-budget-standalone.html | collateral |  |
| ~\Downloads\Turner_Lilly_Submission_Package\Option 1\Option_1_What_Changed_standalone.html | docs/clients/turner/lilly/submission-package/option-1/2026-05-16-option-1-what-changed-standalone.html | collateral |  |
| ~\Downloads\Turner_Lilly_Submission_Package\Option 1\Turner_Lilly_Budget_2026_OPTION1.xlsx | docs/clients/turner/lilly/submission-package/option-1/2026-05-16-turner-lilly-budget-2026-option1.xlsx | collateral |  |
| ~\Downloads\Turner_Lilly_Submission_Package\Option 1\Turner_Lilly_Budget_Narrative_OPTION1.docx | docs/clients/turner/lilly/submission-package/option-1/2026-05-16-turner-lilly-budget-narrative-option1.docx | collateral |  |
| ~\Downloads\Turner_Lilly_Submission_Package\Option 1\Turner_Lilly_What_Changed_OPTION1.docx | docs/clients/turner/lilly/submission-package/option-1/2026-05-16-turner-lilly-what-changed-option1.docx | collateral |  |
| ~\Downloads\Turner_Lilly_Submission_Package\Option 2\Option_2_Strategy_Memo_standalone.html | docs/clients/turner/lilly/submission-package/option-2/2026-05-16-option-2-strategy-memo-standalone.html | collateral |  |
| ~\Downloads\Turner_Lilly_Submission_Package\Option 2\Option_2_Summary_Budget_standalone.html | docs/clients/turner/lilly/submission-package/option-2/2026-05-16-option-2-summary-budget-standalone.html | collateral |  |
| ~\Downloads\Turner_Lilly_Submission_Package\Option 2\Turner_Lilly_Budget_2026_OPTION2.xlsx | docs/clients/turner/lilly/submission-package/option-2/2026-05-16-turner-lilly-budget-2026-option2.xlsx | collateral |  |
| ~\Downloads\Turner_Lilly_Submission_Package\Option 2\Turner_Lilly_Budget_Narrative_OPTION2.docx | docs/clients/turner/lilly/submission-package/option-2/2026-05-16-turner-lilly-budget-narrative-option2.docx | collateral |  |
| ~\Downloads\Turner_Lilly_Submission_Package\Option 2\Turner_Lilly_Strategy_Memo_OPTION2.docx | docs/clients/turner/lilly/submission-package/option-2/2026-05-16-turner-lilly-strategy-memo-option2.docx | collateral |  |
| ~\Dropbox\Turner\Institutional Manuals\Appraisal - Part 1.docx | docs/clients/turner/manuals/2026-04-21-appraisal-part-1.docx | report |  |
| ~\Dropbox\Turner\Institutional Manuals\Appraisal - Part 2.docx | docs/clients/turner/manuals/2026-04-21-appraisal-part-2.docx | report |  |
| ~\Dropbox\Turner\Institutional Manuals\Appraisal - Part 3.docx | docs/clients/turner/manuals/2026-04-21-appraisal-part-3.docx | report |  |
| ~\Dropbox\Turner\Institutional Manuals\Facilities Manual.docx | docs/clients/turner/manuals/2026-04-21-facilities-manual.docx | report |  |
| ~\Dropbox\Turner\Institutional Manuals\Operational Manual.docx | docs/clients/turner/manuals/2026-04-21-operational-manual.docx | report |  |
| ~\Dropbox\Turner\Institutional Manuals\Financial Policy.docx | docs/clients/turner/manuals/2026-04-29-financial-policy.docx | report |  |
| ~\Dropbox\Meridia\files\TTS_State_of_Institution_Financial_Report.pptx | docs/clients/turner/presentations/2026-03-01-tts-state-of-institution-financial-report.pptx | report |  |
| ~\Dropbox\Meridia\Turner State of Institution FY2025 Audit.pptx | docs/clients/turner/presentations/2026-03-18-turner-state-of-institution-fy2025-audit.pptx | report |  |
| ~\Dropbox\Turner\files\TTS_5Year_Budget_Overview.pptx | docs/clients/turner/presentations/2026-04-08-tts-5year-budget-overview.pptx | report |  |
| ~\Dropbox\Turner\files\TTS_Audit_Summary_April_2026.pptx | docs/clients/turner/presentations/2026-04-08-tts-audit-summary-april-2026.pptx | report |  |
| ~\Dropbox\Turner\files\TTS_Board_Report_April_2026.pptx | docs/clients/turner/presentations/2026-04-08-tts-board-report-april-2026.pptx | report |  |
| ~\Dropbox\Turner\files\TTS_Housing_Transition_April_2026.pptx | docs/clients/turner/presentations/2026-04-08-tts-housing-transition-april-2026.pptx | report |  |
| ~\Dropbox\Turner\files\TTS_State_of_Institution_April_2026.pptx | docs/clients/turner/presentations/2026-04-08-tts-state-of-institution-april-2026.pptx | report |  |
| ~\Dropbox\Turner\President Reports\Board Meeting\President's April 2026 Board of Trustees Report.pdf | docs/clients/turner/presentations/2026-04-26-presidents-april-2026-board-of-trustees-report.pdf | report | large .docx source versions left in Dropbox |
| ~\Dropbox\Turner\President Reports\Board Meeting\TTS FY2025 Audited Financial Presentation — Board of Trustees April 2026.pdf | docs/clients/turner/presentations/2026-04-26-tts-fy2025-audited-financial-presentation-board-of-trustees-april-2026.pdf | report |  |
| ~\Dropbox\Turner\President Reports\Board Meeting\TTS_FY2025_Audit_Talking_Points.docx | docs/clients/turner/presentations/2026-04-27-tts-fy2025-audit-talking-points.docx | report |  |
| ~\Dropbox\Claude\tts_authnet_reporting.py | docs/clients/turner/tools/tts_authnet_reporting.py | spec | Authorize.net reporting script for TTS |

### Left behind (grouped)

- **Meridia_Ingestion\Turner Theological Seminary\* (~2,950 files)** — The seminary's institutional records: Accounting, Gusto payroll, QuickBooks, Investment Statements, Audit workpapers, Accreditation (SACS/TRACS), Advancement, Facilities, CTB, WPG, Pinnacle, PayPal/CashApp/Amazon records, board minutes, weekly task sheets. Client operational data — does not belong in a product repo a collaborator may access.
- **Dropbox\Turner\TTS Grant-It\* (557 files)** — Grant-search result dumps; data corpus, not work product.
- **Dropbox\Turner\Facilities, Student Accounts, Branding Concepts (Clothing), G6 BOT Minutes, SACSCOC, Security Reports, Business & Finance, Financial Reports (~610 files)** — Client operational records, raw student account data, board minutes, merch concepts.
- **Dropbox\Turner\President Reports remainder (~35 files)** — Working spreadsheets (budget v actuals), invoices, hotel proposal, SACSCOC budgets, superseded Phase III revisions (v2/v3, prior multi-file PDFs), and 27–31 MB .docx source versions of the migrated board-report PDF.
- **Dropbox\Turner\Artifacts\* (16 files)** — Raw logo PNGs and presidential portraits — client brand assets; the Brand Guide PDF was migrated instead.
- **Grants: W-9, duplicate/unexecuted form copies (~7 files)** — W-9 contains TIN (sensitive, never committed); earlier unexecuted versions superseded by executed copies.
- **Downloads: duplicate Lilly RFP folder variants, Capital Campaign asset/upload duplicates, copier scans, chart of accounts (~95 files)** — Three duplicate copies of the same Revised Budget Package; logo/design dups of files migrated from canonical locations; raw client records.
- **Dropbox\Meridia: Spring 2026 Gammon President's Report.pdf** — Gammon is a different seminary — not Turner, not ASAM. Question to close: is Gammon a second client engagement?


## Third pass — 2026-06-11

| Source | Destination | Classification | Note |
|---|---|---|---|
| (session upload) Turner_Dashboard_Populi_Meeting_Deck.pptx | specs/plumbline/2026-06-11-turner-dashboard-populi-meeting-deck.pptx | spec | source material for spec-v1 |
