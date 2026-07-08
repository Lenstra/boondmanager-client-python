# BoondManager client — API index (generated, do not edit)

One line per endpoint method of `client.api`. Grep this file to find the
right call, then read its docstring in `boondmanager/api.py` for query
parameters and body schema.

Conventions:

- `client.api.<group>.<method>(...)` — all methods are async and return a
  `boondmanager.jsonapi.Document` (dict-compatible; `.one`/`.many`/`.included()`).
- `params` marked with `*` are required query parameters.
- Prefer the higher-level layers when they cover your need:
  `client.fetch_timesheet(id)` for timesheet editing (see
  `boondmanager/timesheets.py`), and the curated helpers on
  `BoondManagerClient` (`get_times_report`, `create_absences_report`, ...).


## client.api.absences (/absences)

- `search()` — GET /absences — Search absences

## client.api.absences_reports (/absences-reports)

- `search(params={startMonth*, endMonth*})` — GET /absences-reports — Search request absences
- `create(body)` — POST /absences-reports — Create a request of absences
- `default(params={resource*})` — GET /absences-reports/default — Get empty request of absences default basic data
- `delete(id)` — DELETE /absences-reports/{id} — Delete the request of absences
- `get(id)` — GET /absences-reports/{id} — Get request of absences basic data
- `update(id, body)` — PUT /absences-reports/{id} — Update basic data related to a request of absences
- `download(id)` — GET /absences-reports/{id}/download — Get request of absences formatted file content
- `reject(id, body)` — POST /absences-reports/{id}/reject — Reject a request of absence
- `rights(id)` — GET /absences-reports/{id}/rights — Get requets of absences rights
- `unvalidate(id, body, params={expectedValidator*})` — POST /absences-reports/{id}/unvalidate — Unvalidate a request of absence
- `validate(id, body, params={expectedValidator*})` — POST /absences-reports/{id}/validate — Validate a request of absence

## client.api.accounts (/accounts)

- `search()` — GET /accounts — Search accounts
- `create(body)` — POST /accounts — Create an account
- `default()` — GET /accounts/default — Get empty account's default basic data
- `delete(id)` — DELETE /accounts/{id} — Delete the account
- `get(id)` — GET /accounts/{id} — Get account's basic data
- `update(id, body)` — PUT /accounts/{id} — Update basic data related to an account
- `connect(id)` — GET /accounts/{id}/connect — Connect to this account

## client.api.actions (/actions)

- `search()` — GET /actions — Search actions entity (Resource, Candidate, Project, Opportunity, Order, Invoice, Contact)
- `create(body)` — POST /actions — Create an action
- `default()` — GET /actions/default — Get empty action's default basic data
- `templates()` — GET /actions/templates — Search templates
- `post_templates(body)` — POST /actions/templates — Create a template
- `delete_templates_by_id(id)` — DELETE /actions/templates/{id} — Delete the template
- `templates_by_id(id)` — GET /actions/templates/{id} — Get template's data
- `update_templates_by_id(id, body)` — PUT /actions/templates/{id} — Update data related to a template
- `delete(id)` — DELETE /actions/{id} — Delete the action
- `get(id)` — GET /actions/{id} — Get action's basic data
- `update(id, body)` — PUT /actions/{id} — Update basic data related to an action
- `attached_flags(id)` — GET /actions/{id}/attached-flags — Get action's attached flags
- `rights(id)` — GET /actions/{id}/rights — Get action's rights

## client.api.administrator (/administrator)

- `search()` — GET /administrator — Get customer's administrator basic data
- `delete_logo()` — DELETE /administrator/logo — Delete the logo
- `update_logo(body)` — PUT /administrator/logo — Update logo

## client.api.advantages (/advantages)

- `create(body)` — POST /advantages — Create an advantage
- `default(params={resource*})` — GET /advantages/default — Get empty advantage's default basic data
- `delete(id)` — DELETE /advantages/{id} — Delete the advantage
- `get(id)` — GET /advantages/{id} — Get advantage's basic data
- `update(id, body)` — PUT /advantages/{id} — Update basic data related to an advantage
- `rights(id)` — GET /advantages/{id}/rights — Get advantage's rights

## client.api.agencies (/agencies)

- `search()` — GET /agencies — Search agencies
- `create(body)` — POST /agencies — Create an agency
- `default()` — GET /agencies/default — Get empty agency's default information data
- `delete(id)` — DELETE /agencies/{id} — Delete the agency
- `get(id)` — GET /agencies/{id} — Get agency's basic data
- `activity_expenses(id)` — GET /agencies/{id}/activity-expenses — Get agency's activity & expenses data
- `update_activity_expenses(id, body)` — PUT /agencies/{id}/activity-expenses — Update activity & expenses data related to an agency
- `delete_activity_expenses_logo(id)` — DELETE /agencies/{id}/activity-expenses/logo — Delete the logo
- `update_activity_expenses_logo(id, body)` — PUT /agencies/{id}/activity-expenses/logo — Update logo
- `billing(id)` — GET /agencies/{id}/billing — Get agency's billing data
- `update_billing(id, body)` — PUT /agencies/{id}/billing — Update billing data related to an agency
- `delete_billing_logo(id)` — DELETE /agencies/{id}/billing/logo — Delete the logo
- `update_billing_logo(id, body)` — PUT /agencies/{id}/billing/logo — Update logo
- `information(id)` — GET /agencies/{id}/information — Get agency's information data
- `update_information(id, body)` — PUT /agencies/{id}/information — Update information data related to an agency
- `opportunities(id)` — GET /agencies/{id}/opportunities — Get agency's opportunities data
- `update_opportunities(id, body)` — PUT /agencies/{id}/opportunities — Update opportunities data related to an agency
- `products(id)` — GET /agencies/{id}/products — Get agency's products data
- `update_products(id, body)` — PUT /agencies/{id}/products — Update products data related to an agency
- `projects(id)` — GET /agencies/{id}/projects — Get agency's projects data
- `update_projects(id, body)` — PUT /agencies/{id}/projects — Update projects data related to an agency
- `purchases(id)` — GET /agencies/{id}/purchases — Get agency's purchases data
- `update_purchases(id, body)` — PUT /agencies/{id}/purchases — Update purchases data related to an agency
- `resources(id)` — GET /agencies/{id}/resources — Get agency's resources data
- `update_resources(id, body)` — PUT /agencies/{id}/resources — Update resources data related to an agency
- `rights(id)` — GET /agencies/{id}/rights — Get agency's rights
- `technical_data(id)` — GET /agencies/{id}/technical-data — Get agency's technical data customization colors (_only available when feature flag `technical-data-customization` is enabled_)
- `update_technical_data(id, body)` — PUT /agencies/{id}/technical-data — Update technical data customization colors for an agency (_only available when feature flag `technical-data-customization` is enabled_)

## client.api.alerts (/alerts)

- `search()` — GET /alerts — Search alerts entity
- `configuration()` — GET /alerts/configuration — Get alerts settings for administrator
- `update_configuration(body)` — PUT /alerts/configuration — Update administrator alerts settings
- `values(id)` — GET /alerts/{id}/values — Get values for alert

## client.api.analytics (/analytics)

- `reportings_production_by_manager(params={startDate*, endDate*})` — GET /analytics/reportings/production-by-manager — Search production by manager reporting

## client.api.application (/application)

- `assignments()` — GET /application/assignments — Get the list of assignments availables for updating
- `backup_dictionary(body)` — POST /application/backup-dictionary — Backup the specific translations
- `current_user()` — GET /application/current-user — Get current user's data
- `dictionary()` — GET /application/dictionary — Get the specific translations
- `update_dictionary(body)` — PUT /application/dictionary — Update the specific translations
- `download_dictionary()` — GET /application/download-dictionary — Get dictionar's file
- `dump_database(body)` — POST /application/dump-database — Create a dabatase dump
- `dynamic_filters()` — GET /application/dynamic-filters — Get cleaned dynamic filters availables for searching
- `flags()` — GET /application/flags — Get the list of flags availables for searching or updating
- `geocities(params={keywords*})` — GET /application/geocities — Search for cities by name (autosuggest)
- `perimeters()` — GET /application/perimeters — Get the list of perimeters availables for searching
- `read_database(body)` — POST /application/read-database — Read database thanks to a MySQL query
- `update_restore_dictionary(body)` — PUT /application/restore-dictionary — Restore the last specific translations backup
- `settings()` — GET /application/settings — Get the specific settings
- `update_settings(body)` — PUT /application/settings — Update the specific settings
- `status()` — GET /application/status — Get status
- `weekend_and_bank_holidays(params={startDate*, endDate*})` — GET /application/weekendAndBankHolidays — Get the types of days between 2 dates

## client.api.apps (/apps)

- `search()` — GET /apps — Search installed apps
- `absences_accounts_absences_accounts()` — GET /apps/absences-accounts/absences-accounts — Search absences accounts
- `update_absences_accounts_absences_accounts_by_id(id, body)` — PUT /apps/absences-accounts/absences-accounts/{id} — Update basic data related to an absences account
- `absences_accounts_import__absences_accounts(body)` — POST /apps/absences-accounts/import/absences-accounts — Import absences accounts
- `accounting_payroll_companies()` — GET /apps/accounting-payroll/companies — Search companies
- `update_accounting_payroll_companies_by_id(id, body)` — PUT /apps/accounting-payroll/companies/{id} — Update company data related to Sage Interface's customer
- `accounting_payroll_configuration()` — GET /apps/accounting-payroll/configuration — Get app's Sage Interface configuration data
- `update_accounting_payroll_configuration(body)` — PUT /apps/accounting-payroll/configuration — Update accounting configuration data related to Sage Interface's customer
- `accounting_payroll_contracts(params={month*})` — GET /apps/accounting-payroll/contracts — Search contracts
- `accounting_payroll_expenses_reports(params={startMonth*, endMonth*})` — GET /apps/accounting-payroll/expenses-reports — Search expenses
- `accounting_payroll_invoices()` — GET /apps/accounting-payroll/invoices — Search companies
- `accounting_payroll_payments(params={startMonth*, endMonth*})` — GET /apps/accounting-payroll/payments — Search payments
- `accounting_payroll_resources()` — GET /apps/accounting-payroll/resources — Search resources
- `update_accounting_payroll_resources_by_id(id, body)` — PUT /apps/accounting-payroll/resources/{id} — Update resource data related to Sage Interface's customer
- `advanced_candidates_candidates()` — GET /apps/advanced-candidates/candidates — Search candidates
- `post_advanced_candidates_candidates(body)` — POST /apps/advanced-candidates/candidates — Create a candidate
- `advanced_candidates_candidates_default()` — GET /apps/advanced-candidates/candidates/default — Get empty candidate's default specific data
- `advanced_candidates_candidates_by_id(id)` — GET /apps/advanced-candidates/candidates/{id} — Get candidate's specific data
- `update_advanced_candidates_candidates_by_id(id, body)` — PUT /apps/advanced-candidates/candidates/{id} — Update specific data related to a candidate
- `advanced_candidates_candidates_by_id_download(id)` — GET /apps/advanced-candidates/candidates/{id}/download — Get candidate's specific data formatted file content
- `advanced_candidates_candidates_by_id_rights(id)` — GET /apps/advanced-candidates/candidates/{id}/rights — Get candidate's rights
- `advanced_candidates_candidates_by_id_tasks(id)` — GET /apps/advanced-candidates/candidates/{id}/tasks — Get candidate's tasks
- `advanced_candidates_resources_by_id(id)` — GET /apps/advanced-candidates/resources/{id} — Get app's Candidates+ resource configuration data
- `update_advanced_candidates_resources_by_id(id, body)` — PUT /apps/advanced-candidates/resources/{id} — Update resource configuration data related to app's Candidates+
- `advanced_projects_configuration()` — GET /apps/advanced-projects/configuration — Get app's Projects+ configuration data
- `update_advanced_projects_configuration(body)` — PUT /apps/advanced-projects/configuration — Update configuration data related to Projects+'s customer
- `advanced_projects_projects()` — GET /apps/advanced-projects/projects — Search projects
- `advanced_projects_projects_by_id(id)` — GET /apps/advanced-projects/projects/{id} — Get project's specific data
- `update_advanced_projects_projects_by_id(id, body)` — PUT /apps/advanced-projects/projects/{id} — Update specific data related to a project
- `advantages_advantages()` — GET /apps/advantages/advantages — Search advantages
- `answering_validators_answering_machines()` — GET /apps/answering-validators/answering-machines — Search answering machines
- `post_answering_validators_answering_machines(body)` — POST /apps/answering-validators/answering-machines — Create an answering machine.
- `delete_answering_validators_answering_machines_by_id(id)` — DELETE /apps/answering-validators/answering-machines/{id} — Delete the answering machine
- `backup_database_configuration()` — GET /apps/backup-database/configuration — Get app's BackupDatabase configuration data
- `update_backup_database_configuration(body)` — PUT /apps/backup-database/configuration — Update configuration data related to BackupDatabase's customer
- `backup_database_dump_database(body)` — POST /apps/backup-database/dump-database — Dump database
- `celebrations_configuration()` — GET /apps/celebrations/configuration — Get app's Celebrations customer configuration data
- `update_celebrations_configuration(body)` — PUT /apps/celebrations/configuration — Update configuration data related to Celebrations customer, main's tab
- `celebrations_employees_arrival()` — GET /apps/celebrations/employees/arrival — Search resources celebrating their arrival
- `celebrations_employees_birthday()` — GET /apps/celebrations/employees/birthday — Search resources celebrating their birthday
- `celebrations_employees_seniority()` — GET /apps/celebrations/employees/seniority — Search resources celebrating their seniority
- `celebrations_employees_by_id(id)` — GET /apps/celebrations/employees/{id} — Get app's Celebrations resource configuration data
- `update_celebrations_employees_by_id(id, body)` — PUT /apps/celebrations/employees/{id} — Update resource configuration data related to app's Celebrations
- `contracts_contracts()` — GET /apps/contracts/contracts — Search contracts
- `corporama_configuration()` — GET /apps/corporama/configuration — Get app's Corporama configuration data
- `create_activity_documents_resources_by_id(id)` — GET /apps/create-activity-documents/resources/{id} — Get resource's basic data
- `data_closing_closed_periods()` — GET /apps/data-closing/closed-periods — Search closed periods
- `update_data_closing_closed_periods_by_id(id, body)` — PUT /apps/data-closing/closed-periods/{id} — Update specific data related to a closed period
- `data_closing_configuration()` — GET /apps/data-closing/configuration — Get app's DataClosing configuration data
- `update_data_closing_configuration(body)` — PUT /apps/data-closing/configuration — Update configuration data related to DataClosing's customer
- `data_closing_expenses_reports(params={startMonth*, endMonth*})` — GET /apps/data-closing/expenses-reports — Search expenses
- `update_data_closing_expenses_reports_by_id(id, body)` — PUT /apps/data-closing/expenses-reports/{id} — Update specific data related to an expenses
- `data_closing_invoices(params={startDate*, endDate*})` — GET /apps/data-closing/invoices — Search invoices
- `update_data_closing_invoices_by_id(id, body)` — PUT /apps/data-closing/invoices/{id} — Update specific data related to an invoice
- `data_closing_times_reports(params={startMonth*, endMonth*})` — GET /apps/data-closing/times-reports — Search timesheets
- `update_data_closing_times_reports_by_id(id, body)` — PUT /apps/data-closing/times-reports/{id} — Update specific data related to a timesheet
- `digital_workplace_categories()` — GET /apps/digital-workplace/categories — Get app's digital workplace categories
- `post_digital_workplace_categories(body)` — POST /apps/digital-workplace/categories — Add app's digital workplace new category
- `delete_digital_workplace_categories_by_id(id)` — DELETE /apps/digital-workplace/categories/{id} — Delete app's Digital workplace category
- `digital_workplace_categories_by_id(id)` — GET /apps/digital-workplace/categories/{id} — Get app's Digital workplace category data
- `update_digital_workplace_categories_by_id(id, body)` — PUT /apps/digital-workplace/categories/{id} — Update app's Digital workplace category
- `digital_workplace_documents(body)` — POST /apps/digital-workplace/documents — Create a document
- `digital_workplace_documents_viewer()` — GET /apps/digital-workplace/documents/viewer — Search documents for app's viewer.
- `delete_digital_workplace_documents_by_id(id)` — DELETE /apps/digital-workplace/documents/{id} — Delete the document
- `digital_workplace_documents_by_id(id)` — GET /apps/digital-workplace/documents/{id} — Get document content
- `digital_workplace_news()` — GET /apps/digital-workplace/news — Search digital workplace news
- `post_digital_workplace_news(body)` — POST /apps/digital-workplace/news — Add app's digital workplace new news
- `delete_digital_workplace_news_by_id(id)` — DELETE /apps/digital-workplace/news/{id} — Delete app's Digital news category
- `digital_workplace_news_by_id(id)` — GET /apps/digital-workplace/news/{id} — Get app's Digital workplace news data
- `update_digital_workplace_news_by_id(id, body)` — PUT /apps/digital-workplace/news/{id} — Update app's Digital news category
- `doc_templates_configuration()` — GET /apps/doc-templates/configuration — Get app's DocumentsTemplates configuration data
- `doc_templates_templates(params={keywords*})` — GET /apps/doc-templates/templates — Search templates available for an entity (candidate, resource, opportunity, order, purchase, contract, delivery, quotation)
- `post_doc_templates_templates(body)` — POST /apps/doc-templates/templates — Create a template
- `doc_templates_templates_viewer()` — GET /apps/doc-templates/templates/viewer — Search templates for app's viewer.
- `delete_doc_templates_templates_by_id(id)` — DELETE /apps/doc-templates/templates/{id} — Delete the template
- `doc_templates_templates_by_id(id)` — GET /apps/doc-templates/templates/{id} — Get template content
- `update_doc_templates_templates_by_id(id, body)` — PUT /apps/doc-templates/templates/{id} — update template content
- `emailing_absencesreports_by_id(id)` — GET /apps/emailing/absencesreports/{id} — Get app's EMailing absencesreports data, main's tab
- `emailing_candidates_by_id(id)` — GET /apps/emailing/candidates/{id} — Get app's EMailing candidate data
- `emailing_configuration()` — GET /apps/emailing/configuration — Get app's EMailing customer configuration data, main's tab
- `update_emailing_configuration(body)` — PUT /apps/emailing/configuration — Update configuration data related to EMailing customer, main's tab
- `emailing_configuration_connection()` — GET /apps/emailing/configuration/connection — Get app's EMailing test connection results
- `emailing_contacts_by_id(id)` — GET /apps/emailing/contacts/{id} — Get app's EMailing contact data, main's tab
- `emailing_expensesreports_by_id(id)` — GET /apps/emailing/expensesreports/{id} — Get app's EMailing expensesreports data, main's tab
- `emailing_invoices_by_id(id)` — GET /apps/emailing/invoices/{id} — Get app's EMailing invoice data, main's tab
- `emailing_positionings_by_id(id)` — GET /apps/emailing/positionings/{id} — Get app's EMailing positioning data, main's tab
- `emailing_quotations_by_id(id)` — GET /apps/emailing/quotations/{id} — Get app's EMailing quotation data, main's tab
- `emailing_resources_by_id(id)` — GET /apps/emailing/resources/{id} — Get app's EMailing resource data, main's tab
- `emailing_resources_by_id_connection(id)` — GET /apps/emailing/resources/{id}/connection — Get app's EMailing test connection results
- `emailing_resources_by_id_settings(id)` — GET /apps/emailing/resources/{id}/settings — Get app's EMailing resource configuration data, main's tab
- `update_emailing_resources_by_id_settings(id, body)` — PUT /apps/emailing/resources/{id}/settings — Update configuration data related to EMailing resource, main's tab
- `emailing_share(body)` — POST /apps/emailing/share — Share a push/message
- `emailing_templates()` — GET /apps/emailing/templates — Search templates
- `post_emailing_templates(body)` — POST /apps/emailing/templates — Create a template
- `emailing_templates_last_used(params={templateType*})` — GET /apps/emailing/templates/last-used — Get last used template's data
- `delete_emailing_templates_by_id(id)` — DELETE /apps/emailing/templates/{id} — Delete the template
- `emailing_templates_by_id(id)` — GET /apps/emailing/templates/{id} — Get template's data
- `update_emailing_templates_by_id(id, body)` — PUT /apps/emailing/templates/{id} — Update data related to a template.
- `emailing_timesreports_by_id(id)` — GET /apps/emailing/timesreports/{id} — Get app's EMailing timesreports data, main's tab
- `esignature_candidates_default()` — GET /apps/esignature/candidates/default — Get empty esignature's default specific data
- `esignature_esignatures(body)` — POST /apps/esignature/esignatures — Create an esignature
- `delete_esignature_esignatures_by_id(id)` — DELETE /apps/esignature/esignatures/{id} — Delete/cancel esignature's specific data
- `esignature_esignatures_by_id(id)` — GET /apps/esignature/esignatures/{id} — Get esignature's specific data
- `esignature_esignatures_by_id_cancel(id, body)` — POST /apps/esignature/esignatures/{id}/cancel — Cancel an esignature
- `exceptional_activity_companies()` — GET /apps/exceptional-activity/companies — Search companies
- `exceptional_activity_times(params={month*})` — GET /apps/exceptional-activity/times — Search times
- `exceptional_activity_times_by_id(id)` — GET /apps/exceptional-activity/times/{id} — Get time data
- `update_exceptional_activity_times_by_id(id, body)` — PUT /apps/exceptional-activity/times/{id} — Update time data
- `extract_payroll_contracts(params={month*})` — GET /apps/extract-payroll/contracts — Search contracts
- `update_extract_payroll_contracts_by_id(id, body)` — PUT /apps/extract-payroll/contracts/{id} — Update contract data related to app's ExtractPayroll
- `extract_payroll_resources_by_id(id)` — GET /apps/extract-payroll/resources/{id} — Get app's ExtractPayroll resource configuration data
- `update_extract_payroll_resources_by_id(id, body)` — PUT /apps/extract-payroll/resources/{id} — Update resource configuration data related to app's ExtractPayroll
- `extractbi_configuration()` — GET /apps/extractbi/configuration — Get app's ExtractBI configuration data
- `update_extractbi_configuration(body)` — PUT /apps/extractbi/configuration — Update configuration data related to ExtractBI's customer
- `extractbi_requests()` — GET /apps/extractbi/requests — Search requests
- `post_extractbi_requests(body)` — POST /apps/extractbi/requests — Create a request
- `delete_extractbi_requests_by_id(id)` — DELETE /apps/extractbi/requests/{id} — Delete the request
- `extractbi_requests_by_id(id)` — GET /apps/extractbi/requests/{id} — Get request's basic data
- `update_extractbi_requests_by_id(id, body)` — PUT /apps/extractbi/requests/{id} — Update basic data related to a request
- `extractbi_requests_by_id_download(id)` — GET /apps/extractbi/requests/{id}/download — Generate extract file
- `extractbi_templates()` — GET /apps/extractbi/templates — Search templates
- `post_extractbi_templates(body)` — POST /apps/extractbi/templates — Create a template
- `delete_extractbi_templates_by_id(id)` — DELETE /apps/extractbi/templates/{id} — Delete the template
- `extractbi_templates_by_id(id)` — GET /apps/extractbi/templates/{id} — Get view's basic data
- `update_extractbi_templates_by_id(id, body)` — PUT /apps/extractbi/templates/{id} — Update basic data related to a template
- `extractbi_templates_by_id_rights(id)` — GET /apps/extractbi/templates/{id}/rights — Get template's rights
- `extractbi_test(body)` — POST /apps/extractbi/test — Test an a query with extractBI
- `gcalendar_get_event(params={signedRequest*})` — GET /apps/gcalendar/get-event — Get an event inside GCalendar
- `gcalendar_notifications_events(body)` — POST /apps/gcalendar/notifications-events — Receive event's notification from GCalendar
- `delete_gcalendar_remove_event()` — DELETE /apps/gcalendar/remove-event — Remove an event inside GCalendar
- `gcalendar_resources_by_id(id)` — GET /apps/gcalendar/resources/{id} — Get app's GCalendar resource configuration data
- `update_gcalendar_update_event(body)` — PUT /apps/gcalendar/update-event — Update an event inside GCalendar
- `gmail_mails(body)` — POST /apps/gmail/mails — Add the mail like an action to boondmanager's resources/candidates/contacts
- `gmail_mails_by_id_mail(id_mail, params={emails*})` — GET /apps/gmail/mails/{idMail} — Get mail's basic data
- `gmail_resources_by_id(id)` — GET /apps/gmail/resources/{id} — Get app's GMail resource configuration data
- `gviewer_download_by_id(id, params={signedRequest*})` — GET /apps/gviewer/download/{id} — Get document content
- `gviewer_resources_by_id(id)` — GET /apps/gviewer/resources/{id} — Get app's GViewer resource configuration data
- `update_gviewer_resources_by_id(id, body)` — PUT /apps/gviewer/resources/{id} — Update resource configuration data related to app's GViewer
- `gviewer_url_documents(params={signedRequest*})` — GET /apps/gviewer/url-documents — Get URLs to view documents
- `hour_accounts_configuration()` — GET /apps/hour-accounts/configuration — Get app's HourAccount configuration data
- `update_hour_accounts_configuration(body)` — PUT /apps/hour-accounts/configuration — Update configuration data related to HourAccount's customer
- `hour_accounts_houraccounts()` — GET /apps/hour-accounts/houraccounts — Search houraccounts
- `hour_accounts_houraccounts_by_id(id)` — GET /apps/hour-accounts/houraccounts/{id} — Get app's HourAccount data
- `update_hour_accounts_houraccounts_by_id(id, body)` — PUT /apps/hour-accounts/houraccounts/{id} — Update data related to HourAccount
- `hour_accounts_houraccounts_by_id_rights(id)` — GET /apps/hour-accounts/houraccounts/{id}/rights — Get HourAccount's rights
- `hour_accounts_resources_by_id_rights(id)` — GET /apps/hour-accounts/resources/{id}/rights — Get resource's rights
- `hour_accounts_resources_by_id_settings(id)` — GET /apps/hour-accounts/resources/{id}/settings — Get resource's settings basic data
- `update_hour_accounts_resources_by_id_settings(id, body)` — PUT /apps/hour-accounts/resources/{id}/settings — Update basic data related to resource's settings
- `hrflow_configuration()` — GET /apps/hrflow/configuration — Get app's HrFlow configuration data
- `update_hrflow_configuration(body)` — PUT /apps/hrflow/configuration — Update configuration data related to HrFlow's customer
- `hrflow_resumes(body)` — POST /apps/hrflow/resumes — Parse a resume
- `intranet_accounts_resources()` — GET /apps/intranet-accounts/resources — Search resources
- `update_intranet_accounts_resources_by_id(id, body)` — PUT /apps/intranet-accounts/resources/{id} — Update basic data related to a resource
- `markers_markers()` — GET /apps/markers/markers — Search markers
- `delete_microsoft_events_by_id_event(id_event)` — DELETE /apps/microsoft/events/{idEvent} — Delete the event's action on Boond
- `microsoft_events_by_id_event(id_event)` — GET /apps/microsoft/events/{idEvent} — Get event's basic data
- `update_microsoft_events_by_id_event(id_event, body)` — PUT /apps/microsoft/events/{idEvent} — Synchronize an action on a boondmanager's resource/candidate/contact/opportunity/project/order/invoice
- `microsoft_events_by_id_event_find(id_event, params={keywordsType*, keywords*})` — GET /apps/microsoft/events/{idEvent}/find — Search resources, candidates, contacts, opportunities, projects, orders or invoices
- `microsoft_extra_id()` — GET /apps/microsoft/extra-id — Get extraId basic's data inside Microsoft Gadget
- `microsoft_gadget()` — GET /apps/microsoft/gadget — Get Microsoft Office Gadget
- `microsoft_get_event(params={signedRequest*})` — GET /apps/microsoft/get-event — Get an event inside Microsoft Calendar
- `microsoft_mails(body)` — POST /apps/microsoft/mails — Add the mail like an action to boondmanager's resources/candidates/contacts
- `microsoft_mails_by_id_mail(id_mail, params={emails*})` — GET /apps/microsoft/mails/{idMail} — Get mail's basic data
- `microsoft_manifest()` — GET /apps/microsoft/manifest — Get Microsoft Office Manifest
- `delete_microsoft_remove_event()` — DELETE /apps/microsoft/remove-event — Remove an event inside Microsoft Calendar
- `microsoft_resources_by_id(id)` — GET /apps/microsoft/resources/{id} — Get app's Microsoft resource configuration data
- `update_microsoft_update_event(body)` — PUT /apps/microsoft/update-event — Update an event inside Microsoft Calendar
- `organization_charts_nodes(body)` — POST /apps/organization-charts/nodes — Create organization chart's node
- `delete_organization_charts_nodes_by_id(id)` — DELETE /apps/organization-charts/nodes/{id} — Delete the node
- `update_organization_charts_nodes_by_id(id, body)` — PUT /apps/organization-charts/nodes/{id} — Update data related to a node
- `organization_charts_orgcharts(params={type*, id*})` — GET /apps/organization-charts/orgcharts — Search organization charts
- `post_organization_charts_orgcharts(body)` — POST /apps/organization-charts/orgcharts — Create an orgchart
- `delete_organization_charts_orgcharts_by_id(id)` — DELETE /apps/organization-charts/orgcharts/{id} — Delete the organization chart
- `organization_charts_orgcharts_by_id(id)` — GET /apps/organization-charts/orgcharts/{id} — Get organization chart's basic data
- `organization_charts_settings(body)` — POST /apps/organization-charts/settings — Create organization chart's settings
- `delete_organization_charts_settings_by_id(id)` — DELETE /apps/organization-charts/settings/{id} — delete this settings
- `organization_charts_settings_by_id(id)` — GET /apps/organization-charts/settings/{id} — Get settings data
- `update_organization_charts_settings_by_id(id, body)` — PUT /apps/organization-charts/settings/{id} — Update settings data
- `plan_production_resources(params={month*})` — GET /apps/plan-production/resources — Search production plans, absences or times
- `post_production_projects(params={month*})` — GET /apps/post-production/projects — Search projects
- `update_post_production_projects_by_id(id, body)` — PUT /apps/post-production/projects/{id} — Update project data related to app's PostProduction
- `post_production_resources_by_id(id)` — GET /apps/post-production/resources/{id} — Get app's PostProduction resource configuration data
- `update_post_production_resources_by_id(id, body)` — PUT /apps/post-production/resources/{id} — Update resource configuration data related to app's PostProduction
- `quotations_quotations()` — GET /apps/quotations/quotations — Search quotations
- `post_quotations_quotations(body)` — POST /apps/quotations/quotations — Create a quotation
- `quotations_quotations_default()` — GET /apps/quotations/quotations/default — Get empty quotation's default information data
- `delete_quotations_quotations_by_id(id)` — DELETE /apps/quotations/quotations/{id} — Delete the quotation
- `quotations_quotations_by_id(id)` — GET /apps/quotations/quotations/{id} — Get quotation's basic data
- `update_quotations_quotations_by_id(id, body)` — PUT /apps/quotations/quotations/{id} — Update basic data related to a quotation
- `quotations_quotations_by_id_download(id)` — GET /apps/quotations/quotations/{id}/download — Get quotation formatted file content
- `quotations_quotations_by_id_rights(id)` — GET /apps/quotations/quotations/{id}/rights — Get quotation's rights
- `quotations_quotations_by_id_send(id, body)` — POST /apps/quotations/quotations/{id}/send — Send invoice by mail
- `quotations_quotations_by_id_tasks(id)` — GET /apps/quotations/quotations/{id}/tasks — Get quotation's tasks
- `resource_planner_projects_by_id(id)` — GET /apps/resource-planner/projects/{id} — Get project's planned times data
- `update_resource_planner_projects_by_id(id, body)` — PUT /apps/resource-planner/projects/{id} — Update project data related to app's ResourcePlanner
- `resource_planner_projects_by_id_rights(id)` — GET /apps/resource-planner/projects/{id}/rights — Get resourceplanner project's rights
- `resource_planner_resources_by_id(id)` — GET /apps/resource-planner/resources/{id} — Get resource's planned times data
- `update_resource_planner_resources_by_id(id, body)` — PUT /apps/resource-planner/resources/{id} — Update resource data related to app's ResourcePlanner
- `resource_planner_resources_by_id_rights(id)` — GET /apps/resource-planner/resources/{id}/rights — Get resourceplanner resource's rights
- `saas_editor_configuration()` — GET /apps/saas-editor/configuration — Get app's SaasEditor configuration data
- `update_saas_editor_configuration(body)` — PUT /apps/saas-editor/configuration — Update configuration data related to SaasEditor's customer
- `saas_editor_reporting(params={startDate*})` — GET /apps/saas-editor/reporting — Search reporting
- `sepa_companies_by_id(id)` — GET /apps/sepa/companies/{id} — Get company's specific data
- `update_sepa_companies_by_id(id, body)` — PUT /apps/sepa/companies/{id} — Update specific data related to a company
- `sepa_configuration()` — GET /apps/sepa/configuration — Get app's Sepa configuration data
- `update_sepa_configuration(body)` — PUT /apps/sepa/configuration — Update configuration data related to Sepa's customer
- `sepa_contracts()` — GET /apps/sepa/contracts — Search contracts
- `sepa_contracts_by_id(id)` — GET /apps/sepa/contracts/{id} — Get contract's specific data
- `update_sepa_contracts_by_id(id, body)` — PUT /apps/sepa/contracts/{id} — Update specific data related to a contract
- `sepa_import__contracts(body)` — POST /apps/sepa/import/contracts — Import contracts bank detail
- `sepa_import__orders(body)` — POST /apps/sepa/import/orders — Import contracts bank detail
- `sepa_import__purchases(body)` — POST /apps/sepa/import/purchases — Import contracts bank detail
- `sepa_import__transfers(body)` — POST /apps/sepa/import/transfers — Import contracts transfers
- `sepa_invoices(params={month*, creditNote*})` — GET /apps/sepa/invoices — Search invoices or credit notes
- `sepa_orders()` — GET /apps/sepa/orders — Search orders
- `sepa_orders_by_id(id)` — GET /apps/sepa/orders/{id} — Get order's specific data
- `update_sepa_orders_by_id(id, body)` — PUT /apps/sepa/orders/{id} — Update specific data related to an order
- `sepa_payments(params={month*})` — GET /apps/sepa/payments — Search payments
- `sepa_purchases()` — GET /apps/sepa/purchases — Search purchases
- `sepa_purchases_by_id(id)` — GET /apps/sepa/purchases/{id} — Get purchase's specific data
- `update_sepa_purchases_by_id(id, body)` — PUT /apps/sepa/purchases/{id} — Update specific data related to a purchase
- `special_reporting_reporting(params={month*})` — GET /apps/special-reporting/reporting — Generate reporting file
- `survey_configuration()` — GET /apps/survey/configuration — Get app's Survey configuration data
- `update_survey_configuration(body)` — PUT /apps/survey/configuration — Update configuration data related to Survey's customer
- `survey_enquiries_by_id(id)` — GET /apps/survey/enquiries/{id} — Get enquiry's basic data
- `update_survey_enquiries_by_id(id, body)` — PUT /apps/survey/enquiries/{id} — Update basic data related to an enquiry
- `survey_enquiries_by_id_rights(id)` — GET /apps/survey/enquiries/{id}/rights — Get enquiry's rights
- `survey_satisfaction_indicators()` — GET /apps/survey/satisfaction-indicators — Search satisfaction indicators
- `survey_satisfactions()` — GET /apps/survey/satisfactions — Search satisfactions
- `install(app_code, body)` — POST /apps/{appCode}/install — Install App
- `delete_uninstall(app_code)` — DELETE /apps/{appCode}/uninstall — Uninstall App
- `entities(app_id)` — GET /apps/{appId}/entities — Search app entities (Only for moduleNoCode's app)
- `post_entities(app_id, body)` — POST /apps/{appId}/entities — Create an app entity (Only for moduleNoCode's app)
- `entities_default(app_id)` — GET /apps/{appId}/entities/default — Get empty app entity's default data
- `entities_dependson(app_id)` — GET /apps/{appId}/entities/dependson — Get app entity's from dependsOn, or create it if does not exist (Only for sectionNoCode's app)
- `delete_entities_by_id(app_id, id)` — DELETE /apps/{appId}/entities/{id} — Delete the app entity
- `entities_by_id(app_id, id)` — GET /apps/{appId}/entities/{id} — Get app entity's basic data
- `entities_by_id_attached_flags(app_id, id)` — GET /apps/{appId}/entities/{id}/attached-flags — Get app entity's attached flags
- `entities_by_id_rights(app_id, id)` — GET /apps/{appId}/entities/{id}/rights — Get app entity's rights
- `entities_by_id_tasks(app_id, id)` — GET /apps/{appId}/entities/{id}/tasks — Get app entity's tasks
- `get(id)` — GET /apps/{id} — Get app's basic data

## client.api.attached_flags (/attached-flags)

- `delete_many(params={flag*})` — DELETE /attached-flags — Delete an attached flag
- `create(body)` — POST /attached-flags — Create an attached flag

## client.api.banking_accounts (/banking-accounts)

- `search()` — GET /banking-accounts — Search banking accounts

## client.api.banking_transactions (/banking-transactions)

- `search()` — GET /banking-transactions — Search banking transactions
- `get(id)` — GET /banking-transactions/{id} — get the banking transaction
- `update(id, body)` — PUT /banking-transactions/{id} — Update the banking transaction

## client.api.billing_deliveries_purchases_balance (/billing-deliveries-purchases-balance)

- `search()` — GET /billing-deliveries-purchases-balance — Search deliveries or purchases with a billing balance

## client.api.billing_details (/billing-details)

- `search()` — GET /billing-details — Search billing details
- `create(body)` — POST /billing-details — Create a billing detail
- `analyze(body)` — POST /billing-details/analyze — Analyze billing details to validate VAT numbers and registration numbers.
- `delete(id)` — DELETE /billing-details/{id} — Delete the billing detail
- `get(id)` — GET /billing-details/{id} — Get billing detail's data
- `update(id, body)` — PUT /billing-details/{id} — Update billing detail's data

## client.api.billing_monthly_balance (/billing-monthly-balance)

- `search(params={startMonth*})` — GET /billing-monthly-balance — Search orders with a monthly billing balance

## client.api.billing_projects_balance (/billing-projects-balance)

- `search()` — GET /billing-projects-balance — Search projects with a billing balance

## client.api.billing_schedules_balance (/billing-schedules-balance)

- `search()` — GET /billing-schedules-balance — Search schedules with a billing balance

## client.api.boondmanager_contracts (/boondmanager-contracts)

- `get(id)` — GET /boondmanager-contracts/{id} — Get boondmanager contract's basic data
- `update(id, body)` — PUT /boondmanager-contracts/{id} — Update basic data related to a contract

## client.api.business_units (/business-units)

- `search()` — GET /business-units — Search business units
- `create(body)` — POST /business-units — Create a business units
- `default()` — GET /business-units/default — Get empty business unit's default information data
- `delete(id)` — DELETE /business-units/{id} — Delete the business unit
- `get(id)` — GET /business-units/{id} — Get business unit's basic data
- `update(id, body)` — PUT /business-units/{id} — Update basic data related to a business unit

## client.api.calendars (/calendars)

- `search()` — GET /calendars — Search calendars
- `default()` — GET /calendars/default — Get empty calendar's default data
- `get(id)` — GET /calendars/{id} — Get calendar's basic data
- `update(id, body)` — PUT /calendars/{id} — Update basic data related to a calendar

## client.api.candidates (/candidates)

- `search()` — GET /candidates — Search candidates
- `create(body)` — POST /candidates — Create a candidate
- `default()` — GET /candidates/default — Get empty candidate's default information data
- `delete(id)` — DELETE /candidates/{id} — Delete the candidate
- `get(id)` — GET /candidates/{id} — Get candidate's basic data
- `actions(id)` — GET /candidates/{id}/actions — Get candidate's actions
- `administrative(id)` — GET /candidates/{id}/administrative — Get candidate's administrative data
- `update_administrative(id, body)` — PUT /candidates/{id}/administrative — Update administrative data related to a candidate
- `ai_matching(id)` — GET /candidates/{id}/ai/matching — Get list of opportunities matching this candidate
- `ai_summary(id)` — GET /candidates/{id}/ai/summary — Get ai generated resource's summary
- `attached_flags(id)` — GET /candidates/{id}/attached-flags — Get candidate's attached flags
- `download(id)` — GET /candidates/{id}/download — Get resource's formatted file content
- `information(id)` — GET /candidates/{id}/information — Get candidate's information data
- `update_information(id, body)` — PUT /candidates/{id}/information — Update information data related to a candidate
- `merge(id, body)` — POST /candidates/{id}/merge — Test a merge or start a merge between two candidates.
- `positionings(id)` — GET /candidates/{id}/positionings — Get candidate's positionings
- `rights(id)` — GET /candidates/{id}/rights — Get candidate's rights
- `tasks(id)` — GET /candidates/{id}/tasks — Get candidate's tasks
- `technical_data(id)` — GET /candidates/{id}/technical-data — Get candidate's technical data
- `update_technical_data(id, body)` — PUT /candidates/{id}/technical-data — Update technical data related to a candidate
- `technical_datas(id)` — GET /candidates/{id}/technical-datas — Get candidate's technical datas

## client.api.companies (/companies)

- `search()` — GET /companies — Search companies
- `create(body)` — POST /companies — Create a company
- `default()` — GET /companies/default — Get empty company's default information data
- `delete(id)` — DELETE /companies/{id} — Delete the company
- `get(id)` — GET /companies/{id} — Get company's basic data
- `actions(id)` — GET /companies/{id}/actions — Get company's actions
- `attached_flags(id)` — GET /companies/{id}/attached-flags — Get company's attached flags
- `contacts(id)` — GET /companies/{id}/contacts — Get company's contacts
- `information(id)` — GET /companies/{id}/information — Get company's information data
- `update_information(id, body)` — PUT /companies/{id}/information — Update information data related to a company
- `invoices(id)` — GET /companies/{id}/invoices — Get company's invoices
- `merge(id, body)` — POST /companies/{id}/merge — Test a merge or start a merge between two companies.
- `opportunities(id)` — GET /companies/{id}/opportunities — Get company's opportunities
- `orders(id)` — GET /companies/{id}/orders — Get company's orders
- `projects(id)` — GET /companies/{id}/projects — Get company's projects
- `provider_invoices(id)` — GET /companies/{id}/provider-invoices — Get company's provider invoices
- `purchases(id)` — GET /companies/{id}/purchases — Get company's purchases
- `rights(id)` — GET /companies/{id}/rights — Get company's rights
- `settings(id)` — GET /companies/{id}/settings — Get company's setting data
- `update_settings(id, body)` — PUT /companies/{id}/settings — Update setting data related to a company
- `tasks(id)` — GET /companies/{id}/tasks — Get company's tasks

## client.api.conditional_fields (/conditional-fields)

- `search()` — GET /conditional-fields — Search conditional fields rules.
- `create(body)` — POST /conditional-fields — Create a conditional field
- `default()` — GET /conditional-fields/default — Get empty conditional field's default basic data
- `delete(id)` — DELETE /conditional-fields/{id} — Delete the conditional field
- `get(id)` — GET /conditional-fields/{id} — Get conditional field's basic data
- `update(id, body)` — PUT /conditional-fields/{id} — Update basic data related to a conditional field

## client.api.contacts (/contacts)

- `search()` — GET /contacts — Search contacts
- `create(body)` — POST /contacts — Create a contact
- `default(params={company*})` — GET /contacts/default — Get empty contact's default information data
- `delete(id)` — DELETE /contacts/{id} — Delete the contact
- `get(id)` — GET /contacts/{id} — Get contact's basic data
- `actions(id)` — GET /contacts/{id}/actions — Get contact's actions
- `attached_flags(id)` — GET /contacts/{id}/attached-flags — Get contact's attached flags
- `information(id)` — GET /contacts/{id}/information — Get contact's information data
- `update_information(id, body)` — PUT /contacts/{id}/information — Update information data related to a contact
- `invoices(id)` — GET /contacts/{id}/invoices — Get contact's invoices
- `merge(id, body)` — POST /contacts/{id}/merge — Test a merge or start a merge between two contacts.
- `opportunities(id)` — GET /contacts/{id}/opportunities — Get contact's opportunities
- `orders(id)` — GET /contacts/{id}/orders — Get contact's orders
- `projects(id)` — GET /contacts/{id}/projects — Get contact's projects
- `purchases(id)` — GET /contacts/{id}/purchases — Get contact's purchases
- `rights(id)` — GET /contacts/{id}/rights — Get contact's rights
- `tasks(id)` — GET /contacts/{id}/tasks — Get contact's tasks

## client.api.contracts (/contracts)

- `create(body)` — POST /contracts — Create a contract
- `default()` — GET /contracts/default — Get empty contract's default basic data
- `delete(id)` — DELETE /contracts/{id} — Delete the contract
- `get(id)` — GET /contracts/{id} — Get contract's basic data
- `update(id, body)` — PUT /contracts/{id} — Update basic data related to a contract
- `advantages(id)` — GET /contracts/{id}/advantages — Get contract's advantages
- `download(id)` — GET /contracts/{id}/download — Get contract formatted file content
- `rights(id)` — GET /contracts/{id}/rights — Get contract's rights
- `tasks(id)` — GET /contracts/{id}/tasks — Get contract's tasks

## client.api.dashboards (/dashboards)

- `search()` — GET /dashboards — Search dashboards for Current User
- `create(body)` — POST /dashboards — Create a dashboard
- `delete(id)` — DELETE /dashboards/{id} — Delete the dashboard
- `get(id)` — GET /dashboards/{id} — Get dashboard's basic data
- `update(id, body)` — PUT /dashboards/{id} — Update dashboard's basic data

## client.api.deliveries (/deliveries)

- `create(body)` — POST /deliveries — Create a delivery
- `delete(id)` — DELETE /deliveries/{id} — Delete the delivery
- `get(id)` — GET /deliveries/{id} — Get delivery's basic data
- `update(id, body)` — PUT /deliveries/{id} — Update basic data related to a delivery
- `advantages(id)` — GET /deliveries/{id}/advantages — Get delivery's advantages
- `delivery_order_download(id, params={deliveryOrder*})` — GET /deliveries/{id}/delivery-order-download — Get delivery formatted file content
- `download(id)` — GET /deliveries/{id}/download — Get delivery formatted file content
- `renew(id, body)` — POST /deliveries/{id}/renew — Renew this delivery by creating a new one
- `rights(id)` — GET /deliveries/{id}/rights — Get delivery's rights
- `send(id, body)` — POST /deliveries/{id}/send — Send delivery's formatted filed by mail
- `tasks(id)` — GET /deliveries/{id}/tasks — Get delivery's tasks

## client.api.deliveries_groupments (/deliveries-groupments)

- `search()` — GET /deliveries-groupments — Search deliveries & groupments

## client.api.devices (/devices)

- `delete(id)` — DELETE /devices/{id} — Delete the device
- `delete_session(id)` — DELETE /devices/{id}/session — Delete the session

## client.api.documents (/documents)

- `create(body)` — POST /documents — Create a document
- `viewer()` — GET /documents/viewer — Search documents for app's viewer.
- `delete(id)` — DELETE /documents/{id} — Delete the document
- `get(id)` — GET /documents/{id} — Get document content
- `update(id, body)` — PUT /documents/{id} — Update information data related to a document

## client.api.download_center (/download-center)

- `search()` — GET /download-center — Manage download center
- `delete_by_folder(perimeter_manager, folder)` — DELETE /download-center/{perimeterManager}/{folder} — Delete the download center's folder
- `by_folder(perimeter_manager, folder)` — GET /download-center/{perimeterManager}/{folder} — Search download center's files
- `by_folder_download(perimeter_manager, folder)` — GET /download-center/{perimeterManager}/{folder}/download — Get download center's folder content
- `delete_by_folder_visitor_access(perimeter_manager, folder)` — DELETE /download-center/{perimeterManager}/{folder}/visitor-access — Delete the visitor access to a download center's file
- `by_folder_visitor_access(perimeter_manager, folder, body)` — POST /download-center/{perimeterManager}/{folder}/visitor-access — Create a visitor access to a download center's file
- `delete_by_folder_by_file(perimeter_manager, folder, file)` — DELETE /download-center/{perimeterManager}/{folder}/{file} — Delete the download center's file
- `by_folder_by_file(perimeter_manager, folder, file)` — GET /download-center/{perimeterManager}/{folder}/{file} — Get download center's file content

## client.api.e_invoicing (/e-invoicing)

- `schemes()` — GET /e-invoicing/schemes — get e-invoicing schemes

## client.api.expenses (/expenses)

- `search()` — GET /expenses — Search expenses

## client.api.expenses_reports (/expenses-reports)

- `search(params={startMonth*, endMonth*})` — GET /expenses-reports — Search expenses
- `create(body)` — POST /expenses-reports — Create an expenses
- `default(params={resource*, term*})` — GET /expenses-reports/default — Get empty expenses default basic data
- `delete(id)` — DELETE /expenses-reports/{id} — Delete the expenses
- `get(id)` — GET /expenses-reports/{id} — Get expenses basic data
- `update(id, body)` — PUT /expenses-reports/{id} — Update basic data related to an expenses
- `certification(id, body)` — POST /expenses-reports/{id}/certification — Launch certification on expensesreport
- `download(id, params={type*})` — GET /expenses-reports/{id}/download — Get expenses formatted file content
- `pay(id, body)` — POST /expenses-reports/{id}/pay — Pay an expenses
- `reject(id, body)` — POST /expenses-reports/{id}/reject — Reject an expenses
- `rights(id)` — GET /expenses-reports/{id}/rights — Get expenses rights
- `unvalidate(id, body, params={expectedValidator*})` — POST /expenses-reports/{id}/unvalidate — Unvalidate an expenses
- `validate(id, body, params={expectedValidator*})` — POST /expenses-reports/{id}/validate — Validate an expenses

## client.api.flags (/flags)

- `search()` — GET /flags — Search flags
- `create(body)` — POST /flags — Create a flag
- `delete(id)` — DELETE /flags/{id} — Delete the flag
- `get(id)` — GET /flags/{id} — Get flag's basic data
- `update(id, body)` — PUT /flags/{id} — Update basic data related to a flag

## client.api.followed_documents (/followed-documents)

- `create(body)` — POST /followed-documents — Create a document to follow
- `default()` — GET /followed-documents/default — Get empty document to follow Default's basic data
- `delete(id)` — DELETE /followed-documents/{id} — Delete the document to follow up
- `get(id)` — GET /followed-documents/{id} — Get basic data of document to follow
- `update(id, body)` — PUT /followed-documents/{id} — Update basic data related to a document to follow up
- `rights(id)` — GET /followed-documents/{id}/rights — Get rights of documents to follow

## client.api.forms (/forms)

- `create(body)` — POST /forms — Create a form
- `default()` — GET /forms/default — Get empty form's default basic data
- `templates()` — GET /forms/templates — Search form's templates
- `post_templates(body)` — POST /forms/templates — Create a form's template
- `templates_default()` — GET /forms/templates/default — Get empty form's template's default basic data
- `delete_templates_by_id(id)` — DELETE /forms/templates/{id} — Delete the form's template
- `templates_by_id(id)` — GET /forms/templates/{id} — Get form's template's basic data
- `update_templates_by_id(id, body)` — PUT /forms/templates/{id} — Update form's template's basic data
- `delete(id)` — DELETE /forms/{id} — Delete the form
- `get(id)` — GET /forms/{id} — Get form's basic data
- `update(id, body)` — PUT /forms/{id} — Update form's basic data
- `remind(id, body)` — POST /forms/{id}/remind — Remind a form
- `rights(id)` — GET /forms/{id}/rights — Get form's rights
- `tasks(id)` — GET /forms/{id}/tasks — Get form's tasks

## client.api.gadgets (/gadgets)

- `values(id)` — GET /gadgets/{id}/values — Get gadget's values

## client.api.google (/google)

- `delete(id)` — DELETE /google/{id} — Log out user

## client.api.groupments (/groupments)

- `create(body)` — POST /groupments — Create a groupment
- `default(params={project*})` — GET /groupments/default — Get empty groupment's default information data
- `duplicate(body, params={startDate*, endDate*})` — POST /groupments/duplicate — Duplicate groupment
- `delete(id)` — DELETE /groupments/{id} — Delete the groupment
- `get(id)` — GET /groupments/{id} — Get groupment's basic data
- `update(id, body)` — PUT /groupments/{id} — Update basic data related to a groupment
- `rights(id)` — GET /groupments/{id}/rights — Get groupment's rights

## client.api.import_ (/import)

- `actions(body)` — POST /import/actions — Import actions
- `candidates(body)` — POST /import/candidates — Import candidates
- `contacts(body)` — POST /import/contacts — Import contacts
- `opportunities(body)` — POST /import/opportunities — Import opportunities
- `resources(body)` — POST /import/resources — Import resources

## client.api.inactivities (/inactivities)

- `create(body)` — POST /inactivities — Create an inactivity
- `default(params={resource*})` — GET /inactivities/default — Get empty inactivity's default information data
- `delete(id)` — DELETE /inactivities/{id} — Delete the inactivity
- `get(id)` — GET /inactivities/{id} — Get inactivity's basic data
- `update(id, body)` — PUT /inactivities/{id} — Update basic data related to an inactivity
- `rights(id)` — GET /inactivities/{id}/rights — Get inactivity's rights

## client.api.invoices (/invoices)

- `search()` — GET /invoices — Search invoices
- `create(body)` — POST /invoices — Create an invoice depending on query parameters
- `bulk_send(body)` — POST /invoices/bulk-send — Bulk send invoices and update state after
- `cart(params={order*, startDate*, endDate*})` — GET /invoices/cart — Get new invoice data from cart definition
- `default(params={order*})` — GET /invoices/default — Get empty invoice's default information data
- `delete(id)` — DELETE /invoices/{id} — Delete the invoice
- `get(id)` — GET /invoices/{id} — Get invoice's basic data
- `actions(id)` — GET /invoices/{id}/actions — Get invoice's actions
- `update_adjust(id, body)` — PUT /invoices/{id}/adjust — Adjust invoice
- `attached_flags(id)` — GET /invoices/{id}/attached-flags — Get invoice's attached flags
- `billable_items(id)` — GET /invoices/{id}/billable-items — Get invoice's billable items
- `check(id)` — GET /invoices/{id}/check — Check invoice properties / states (like e-invoicing)
- `download(id)` — GET /invoices/{id}/download — Get invoice formatted file content
- `information(id)` — GET /invoices/{id}/information — Get invoice's information data
- `update_information(id, body)` — PUT /invoices/{id}/information — Update information data related to an invoice
- `preview(id)` — GET /invoices/{id}/preview — Get invoice document
- `rights(id)` — GET /invoices/{id}/rights — Get invoice's rights
- `send(id, body)` — POST /invoices/{id}/send — Send invoice by mail
- `tasks(id)` — GET /invoices/{id}/tasks — Get invoice's tasks

## client.api.invoicing_connections (/invoicing-connections)

- `search()` — GET /invoicing-connections — Search Invoicing connectors
- `create(body)` — POST /invoicing-connections — Create new connector
- `authorize(body)` — POST /invoicing-connections/authorize — Start the OAuth flow for an OAuth-only provider (e.g. Pennylane).
- `callback(params={code*, state*})` — GET /invoicing-connections/callback — Endpoint the OAuth provider redirects the user back to after the consent
- `delete(id)` — DELETE /invoicing-connections/{id} — remove connector
- `get(id)` — GET /invoicing-connections/{id} — get connector's data
- `update(id, body)` — PUT /invoicing-connections/{id} — Update connector's data

## client.api.logs (/logs)

- `search()` — GET /logs — Search logs entity (Resource, Candidate, Project, Opportunity, Order, Invoice, Contact)
- `get(id)` — GET /logs/{id} — Get log's basic data

## client.api.mandatory_leave (/mandatory-leave)

- `search()` — GET /mandatory-leave — Search mandatory leave
- `create(body)` — POST /mandatory-leave — Create a mandatory absence
- `delete(id)` — DELETE /mandatory-leave/{id} — Delete the mandatory leave
- `get(id)` — GET /mandatory-leave/{id} — Get mandatory leave basic data
- `information(id)` — GET /mandatory-leave/{id}/information — Get mandatory leave basic data
- `update_information(id, body)` — PUT /mandatory-leave/{id}/information — Update basic data related to a mandatory leave
- `resources(id)` — GET /mandatory-leave/{id}/resources — Get mandatory leave resources
- `update_resources(id, body)` — PUT /mandatory-leave/{id}/resources — Exclude/include resources in mandatory leave
- `rights(id)` — GET /mandatory-leave/{id}/rights — Get mandatory leave rights

## client.api.marketplace (/marketplace)

- `search()` — GET /marketplace — Search marketplace's apps
- `create(body)` — POST /marketplace — Create a marketplace's apps
- `default()` — GET /marketplace/default — Get empty marketplace's App default information data
- `refresh_token(body)` — POST /marketplace/refresh-token — Refresh App token
- `configure(app_code)` — GET /marketplace/{appCode}/configure — Get marketplace's App access
- `update_configure(app_code, body)` — PUT /marketplace/{appCode}/configure — Update marketplace's App access
- `delete(id)` — DELETE /marketplace/{id} — Delete a marketplace's App
- `get(id)` — GET /marketplace/{id} — Get marketplace's App basic data
- `update(id, body)` — PUT /marketplace/{id} — Update basic data related to a marketplace's App
- `data_visualization(id)` — GET /marketplace/{id}/data-visualization — Get marketplace's App data visualization.
- `install(id, body)` — POST /marketplace/{id}/install — Install marketplace's App
- `delete_logo(id)` — DELETE /marketplace/{id}/logo — Delete the logo
- `update_logo(id, body)` — PUT /marketplace/{id}/logo — Update logo
- `publish(id, body)` — POST /marketplace/{id}/publish — Send publication request by mail
- `rights(id)` — GET /marketplace/{id}/rights — Get marketplace's App rights
- `translations(id)` — GET /marketplace/{id}/translations — Get marketplace's App translations
- `update_translations(id, body)` — PUT /marketplace/{id}/translations — Update marketplace's App translations
- `delete_uninstall(id)` — DELETE /marketplace/{id}/uninstall — Uninstall marketplace's App
- `validate(id, body)` — POST /marketplace/{id}/validate — Validate marketplace's App

## client.api.microsoft (/microsoft)

- `delete(id)` — DELETE /microsoft/{id} — Log out user

## client.api.notifications (/notifications)

- `search(params={category*})` — GET /notifications — Search notification for the current user.
- `update_markas(body)` — PUT /notifications/markas — Update state of all users notification with a specific category.
- `get(id)` — GET /notifications/{id} — Get the notification
- `update(id, body)` — PUT /notifications/{id} — Update part of notification.

## client.api.opportunities (/opportunities)

- `search()` — GET /opportunities — Search opportunities
- `create(body)` — POST /opportunities — Create an opportunity
- `ai_parsing_by_job_id(job_id)` — GET /opportunities/ai/parsing/{jobId} — Retrieve the current status of a parsing job previously created via
- `default()` — GET /opportunities/default — Get empty opportunity's default information data
- `delete(id)` — DELETE /opportunities/{id} — Delete the opportunity
- `get(id)` — GET /opportunities/{id} — Get opportunity's basic data
- `actions(id)` — GET /opportunities/{id}/actions — Get opportunity's actions
- `ai_assistant(id, body)` — POST /opportunities/{id}/ai/assistant — Submit uploaded files, a text description, contact actions and/or voice notes for asynchronous AI parsing.
- `ai_matching(id)` — GET /opportunities/{id}/ai/matching — Get list of profile matching this opportunity
- `attached_flags(id)` — GET /opportunities/{id}/attached-flags — Get opportunity's attached flags
- `download(id)` — GET /opportunities/{id}/download — Get opportunity formatted file content
- `information(id)` — GET /opportunities/{id}/information — Get opportunity's information data
- `update_information(id, body)` — PUT /opportunities/{id}/information — Update information data related to an opportunity
- `positionings(id)` — GET /opportunities/{id}/positionings — Get opportunity's positionings
- `projects(id)` — GET /opportunities/{id}/projects — Get opportunity's projects
- `rights(id)` — GET /opportunities/{id}/rights — Get opportunity's rights
- `simulation(id)` — GET /opportunities/{id}/simulation — Get opportunity's simulation data
- `update_simulation(id, body)` — PUT /opportunities/{id}/simulation — Update simulation data related to an opportunity
- `tasks(id)` — GET /opportunities/{id}/tasks — Get opportunity's tasks

## client.api.orders (/orders)

- `search()` — GET /orders — Search orders
- `create(body)` — POST /orders — Create an order
- `default(params={project*})` — GET /orders/default — Get empty order's default information data
- `delete(id)` — DELETE /orders/{id} — Delete the order
- `get(id)` — GET /orders/{id} — Get order's basic data
- `actions(id)` — GET /orders/{id}/actions — Get order's actions
- `attached_flags(id)` — GET /orders/{id}/attached-flags — Get order's attached flags
- `download(id)` — GET /orders/{id}/download — Get order formatted file content
- `information(id)` — GET /orders/{id}/information — Get order's information data
- `update_information(id, body)` — PUT /orders/{id}/information — Update information data related to an order
- `invoices(id)` — GET /orders/{id}/invoices — Get order's invoices
- `rights(id)` — GET /orders/{id}/rights — Get order's rights
- `tasks(id)` — GET /orders/{id}/tasks — Get order's tasks

## client.api.payments (/payments)

- `search()` — GET /payments — Search payments
- `create(body)` — POST /payments — Create a payment
- `default(params={purchase*})` — GET /payments/default — Get empty payment's default basic data
- `delete(id)` — DELETE /payments/{id} — Delete the payment
- `get(id)` — GET /payments/{id} — Get payment's basic data
- `update(id, body)` — PUT /payments/{id} — Update basic data related to a payment
- `rights(id)` — GET /payments/{id}/rights — Get payment's rights
- `tasks(id)` — GET /payments/{id}/tasks — Get payment's tasks

## client.api.planning_absences (/planning-absences)

- `search(params={startDate*, endDate*})` — GET /planning-absences — Search planning absences

## client.api.poles (/poles)

- `search()` — GET /poles — Search poles
- `create(body)` — POST /poles — Create a pole
- `delete(id)` — DELETE /poles/{id} — Delete the pole
- `get(id)` — GET /poles/{id} — Get pole's basic data
- `update(id, body)` — PUT /poles/{id} — Update basic data related to a pole

## client.api.positionings (/positionings)

- `search()` — GET /positionings — Search positionings
- `create(body)` — POST /positionings — Create a positioning.
- `update_bulk_update(body)` — PUT /positionings/bulk-update — Bulk update positionings
- `delete(id)` — DELETE /positionings/{id} — Delete the positioning
- `get(id)` — GET /positionings/{id} — Get positioning's basic data
- `update(id, body)` — PUT /positionings/{id} — Update basic data related to a positioning.
- `attached_flags(id)` — GET /positionings/{id}/attached-flags — Get positioning's attached flags
- `rights(id)` — GET /positionings/{id}/rights — Get positioning's rights
- `tasks(id)` — GET /positionings/{id}/tasks — Get positioning's tasks

## client.api.products (/products)

- `search()` — GET /products — Search products
- `create(body)` — POST /products — Create a product
- `default()` — GET /products/default — Get empty product's default information data
- `delete(id)` — DELETE /products/{id} — Delete the product
- `get(id)` — GET /products/{id} — Get product's basic data
- `attached_flags(id)` — GET /products/{id}/attached-flags — Get product's attached flags
- `information(id)` — GET /products/{id}/information — Get product's information data
- `update_information(id, body)` — PUT /products/{id}/information — Update information data related to a product
- `opportunities(id)` — GET /products/{id}/opportunities — Get product's opportunities
- `projects(id)` — GET /products/{id}/projects — Get product's projects
- `rights(id)` — GET /products/{id}/rights — Get product's rights
- `tasks(id)` — GET /products/{id}/tasks — Get product's tasks

## client.api.projects (/projects)

- `search()` — GET /projects — Search projects
- `create(body)` — POST /projects — Create a project which mode is only 'product' or `fixed'
- `carts()` — GET /projects/carts — Get project's carts
- `carts_widgets()` — GET /projects/carts/widgets — Get project's carts
- `delete(id)` — DELETE /projects/{id} — Delete the project
- `get(id)` — GET /projects/{id} — Get project's basic data
- `actions(id)` — GET /projects/{id}/actions — Get project's actions
- `advantages(id)` — GET /projects/{id}/advantages — Get project's advantages
- `attached_flags(id)` — GET /projects/{id}/attached-flags — Get project's attached flags
- `batches_markers(id)` — GET /projects/{id}/batches-markers — Get project's batches & markers data
- `update_batches_markers(id, body)` — PUT /projects/{id}/batches-markers — Update batches & markers data related to a project
- `deliveries_groupments(id)` — GET /projects/{id}/deliveries-groupments — Get project's deliveries & groupments
- `information(id)` — GET /projects/{id}/information — Get project's information data
- `update_information(id, body)` — PUT /projects/{id}/information — Update information data related to a project
- `orders(id)` — GET /projects/{id}/orders — Get project's orders
- `productivity(id)` — GET /projects/{id}/productivity — Get projects's productivity data
- `purchases(id)` — GET /projects/{id}/purchases — Get projects's purchases
- `rights(id)` — GET /projects/{id}/rights — Get project's rights
- `simulation(id)` — GET /projects/{id}/simulation — Get project's simulation data
- `update_simulation(id, body)` — PUT /projects/{id}/simulation — Update simulation data related to a project
- `tasks(id)` — GET /projects/{id}/tasks — Get project's tasks

## client.api.provider_invoices (/provider-invoices)

- `search()` — GET /provider-invoices — Search provider invoices
- `create(body)` — POST /provider-invoices — Create a provider invoice
- `default()` — GET /provider-invoices/default — Get empty provider invoice's default basic data
- `delete(id)` — DELETE /provider-invoices/{id} — Delete the provider invoice
- `get(id)` — GET /provider-invoices/{id} — Get provider invoice's basic data
- `update(id, body)` — PUT /provider-invoices/{id} — Update provider invoice's basic data
- `activity_expenses(id)` — GET /provider-invoices/{id}/activity-expenses — Get provider invoice's activity expenses
- `rights(id)` — GET /provider-invoices/{id}/rights — Get provider invoice's rights

## client.api.purchases (/purchases)

- `search()` — GET /purchases — Search purchases
- `create(body)` — POST /purchases — Create a purchase
- `default()` — GET /purchases/default — Get empty purchase's default information data
- `delete(id)` — DELETE /purchases/{id} — Delete the purchase
- `get(id)` — GET /purchases/{id} — Get purchase's basic data
- `attached_flags(id)` — GET /purchases/{id}/attached-flags — Get purchase's attached flags
- `download(id)` — GET /purchases/{id}/download — Get purchase formatted file content
- `information(id)` — GET /purchases/{id}/information — Get purchase's information data
- `update_information(id, body)` — PUT /purchases/{id}/information — Update information data related to a purchase
- `payments(id)` — GET /purchases/{id}/payments — Get purchase's payments
- `rights(id)` — GET /purchases/{id}/rights — Get purchase's rights
- `simulation(id)` — GET /purchases/{id}/simulation — Get purchase's simulation
- `tasks(id)` — GET /purchases/{id}/tasks — Get purchase's tasks

## client.api.reporting_companies (/reporting-companies)

- `search(params={startDate*, endDate*})` — GET /reporting-companies — Search companies reporting

## client.api.reporting_production_plans (/reporting-production-plans)

- `search(params={startDate*, endDate*})` — GET /reporting-production-plans — Search production plans reporting

## client.api.reporting_projects (/reporting-projects)

- `search()` — GET /reporting-projects — Search projects reporting

## client.api.reporting_resources (/reporting-resources)

- `search()` — GET /reporting-resources — Search resources reporting

## client.api.reporting_synthesis (/reporting-synthesis)

- `search(params={startDate*})` — GET /reporting-synthesis — Search synthesis reporting

## client.api.resources (/resources)

- `search()` — GET /resources — Search resources
- `create(body)` — POST /resources — Create a resource
- `default()` — GET /resources/default — Get empty resource's default information data
- `delete(id)` — DELETE /resources/{id} — Delete the resource
- `get(id)` — GET /resources/{id} — Get resource's basic data
- `absences_accounts(id)` — GET /resources/{id}/absences-accounts — Get resource's absences accounts
- `absences_reports(id)` — GET /resources/{id}/absences-reports — Get resource's requests absences
- `actions(id)` — GET /resources/{id}/actions — Get resource's actions
- `administrative(id)` — GET /resources/{id}/administrative — Get resource's administrative data
- `update_administrative(id, body)` — PUT /resources/{id}/administrative — Update administrative data related to a resource
- `advantages(id)` — GET /resources/{id}/advantages — Get resource's advantages
- `ai_matching(id)` — GET /resources/{id}/ai/matching — Get list of opportunities matching this resource
- `ai_summary(id)` — GET /resources/{id}/ai/summary — Get ai generated candidate's summary
- `attached_flags(id)` — GET /resources/{id}/attached-flags — Get resource's attached flags
- `deliveries_inactivities(id)` — GET /resources/{id}/deliveries-inactivities — Get resource's deliveries & inactivities
- `download(id)` — GET /resources/{id}/download — Get resource's formatted file content
- `expenses_reports(id)` — GET /resources/{id}/expenses-reports — Get resource's expenses
- `followed_documents(id)` — GET /resources/{id}/followed-documents — Get resource's documents to follow up
- `forms(id)` — GET /resources/{id}/forms — Search resource's forms
- `information(id)` — GET /resources/{id}/information — Get resource's information data
- `update_information(id, body)` — PUT /resources/{id}/information — Update information data related to a resource.
- `positionings(id)` — GET /resources/{id}/positionings — Get resource's positionings
- `projects(id)` — GET /resources/{id}/projects — Get resource's projects
- `provider_invoices(id)` — GET /resources/{id}/provider-invoices — Get resource's providerinvoices
- `rights(id)` — GET /resources/{id}/rights — Get resource's rights
- `settings_absences_accounts(id)` — GET /resources/{id}/settings/absences-accounts — Get resource's absences accounts settings
- `update_settings_absences_accounts(id, body)` — PUT /resources/{id}/settings/absences-accounts — Update absences accounts related to a resource
- `settings_alerts(id)` — GET /resources/{id}/settings/alerts — Get resource's alerts settings
- `update_settings_alerts(id, body)` — PUT /resources/{id}/settings/alerts — Update resource's alerts settings
- `settings_alerts_reset(id, body)` — POST /resources/{id}/settings/alerts/reset — Reset resource's alerts settings
- `settings_dashboards(id)` — GET /resources/{id}/settings/dashboards — Get resource's dashboard settings
- `settings_groups(id)` — GET /resources/{id}/settings/groups — Get resource's groups settings
- `update_settings_groups(id, body)` — PUT /resources/{id}/settings/groups — Update groups settings related to a resource
- `settings_intranet(id)` — GET /resources/{id}/settings/intranet — Get resource's intranet settings
- `update_settings_intranet(id, body)` — PUT /resources/{id}/settings/intranet — Update intranet settings related to a resource
- `settings_notifications(id)` — GET /resources/{id}/settings/notifications — Get resource's notifications settings
- `update_settings_notifications(id, body)` — PUT /resources/{id}/settings/notifications — Update notifications settings related to a resource
- `settings_positioning_suggests(id)` — GET /resources/{id}/settings/positioning-suggests — Get resource's positioning suggest settings
- `update_settings_positioning_suggests(id, body)` — PUT /resources/{id}/settings/positioning-suggests — Update positioning suggest settings related to a resource
- `settings_reporting(id)` — GET /resources/{id}/settings/reporting — Get resource's reporting settings
- `update_settings_reporting(id, body)` — PUT /resources/{id}/settings/reporting — Update reporting settings related to a resource
- `settings_security(id)` — GET /resources/{id}/settings/security — Get resource's security setting
- `update_settings_security(id, body)` — PUT /resources/{id}/settings/security — Update security setting related to a resource
- `settings_targets(id)` — GET /resources/{id}/settings/targets — Get resource's targets setting
- `tasks(id)` — GET /resources/{id}/tasks — Get resource's tasks
- `technical_data(id)` — GET /resources/{id}/technical-data — Get resource's technical data
- `update_technical_data(id, body)` — PUT /resources/{id}/technical-data — Update technical data related to a resource
- `technical_datas(id)` — GET /resources/{id}/technical-datas — Get resource's technical datas
- `times_reports(id)` — GET /resources/{id}/times-reports — Get resource's timesheets

## client.api.roles (/roles)

- `search()` — GET /roles — Search roles
- `create(body)` — POST /roles — Create a role
- `default()` — GET /roles/default — Get empty role's default basic data
- `templates()` — GET /roles/templates — Search roles
- `post_templates(body)` — POST /roles/templates — Create a role
- `templates_default()` — GET /roles/templates/default — Get empty role's default basic data
- `delete_templates_by_id(id)` — DELETE /roles/templates/{id} — Delete the role
- `templates_by_id(id)` — GET /roles/templates/{id} — Get role's basic data
- `update_templates_by_id(id, body)` — PUT /roles/templates/{id} — Update basic data related to a role
- `delete(id)` — DELETE /roles/{id} — Delete the role
- `get(id)` — GET /roles/{id} — Get role's basic data
- `update(id, body)` — PUT /roles/{id} — Update basic data related to a role

## client.api.sandbox (/sandbox)

- `create(body)` — POST /sandbox — Create a sandbox
- `connect()` — GET /sandbox/connect — Connect to the sandbox

## client.api.savedsearches (/savedsearches)

- `search()` — GET /savedsearches — Search user's saved search
- `create(body)` — POST /savedsearches — Create a saved search
- `delete(id)` — DELETE /savedsearches/{id} — Delete the saved search
- `get(id)` — GET /savedsearches/{id} — Get saved search's basic data
- `update(id, body)` — PUT /savedsearches/{id} — Update basic data related to a saved search

## client.api.share (/share)

- `create(body)` — POST /share — Share a profile
- `default()` — GET /share/default — Get empty share's profile default basic data

## client.api.signature (/signature)

- `delete_many()` — DELETE /signature — Delete sign request
- `search()` — GET /signature — Access signature from visitor access
- `update_many(body)` — PUT /signature — Update signature from visitor access

## client.api.signatures (/signatures)

- `document_by_id(id)` — GET /signatures/document/{id} — Get download center's file content

## client.api.standard_profiles (/standard-profiles)

- `search()` — GET /standard-profiles — Search standard profiles
- `create(body)` — POST /standard-profiles — Create a standard profile
- `default()` — GET /standard-profiles/default — Get empty standard profile's default basic data
- `delete(id)` — DELETE /standard-profiles/{id} — Delete the standard profile
- `get(id)` — GET /standard-profiles/{id} — Get standard profile's basic data
- `update(id, body)` — PUT /standard-profiles/{id} — Update standard profile's basic data
- `rights(id)` — GET /standard-profiles/{id}/rights — Get standard profile's rights

## client.api.subscription (/subscription)

- `search()` — GET /subscription — Get subscription's basic data
- `update_many(body)` — PUT /subscription — Update basic data related to a subscription
- `invoices()` — GET /subscription/invoices — Search invoices
- `invoices_by_id_download(id)` — GET /subscription/invoices/{id}/download — Get subscription's invoice formatted file content

## client.api.targets (/targets)

- `create(body)` — POST /targets — Create a target
- `delete(id)` — DELETE /targets/{id} — Delete the target
- `get(id)` — GET /targets/{id} — Get target's basic data
- `update(id, body)` — PUT /targets/{id} — Update basic data related to a target

## client.api.tasks (/tasks)

- `get(id)` — GET /tasks/{id} — Get a task
- `check(id, body)` — POST /tasks/{id}/check — Check a task
- `uncheck(id, body)` — POST /tasks/{id}/uncheck — Uncheck a task

## client.api.technical_datas (/technical-datas)

- `create(body)` — POST /technical-datas — Create technical data for a resource or candidate
- `default()` — GET /technical-datas/default — Get empty technical Data default basic values
- `visitor_access()` — GET /technical-datas/visitor-access — Public technical file data
- `delete(id)` — DELETE /technical-datas/{id} — Delete the technical data
- `get(id)` — GET /technical-datas/{id} — Get technical data's
- `update(id, body)` — PUT /technical-datas/{id} — Update technical data's
- `update_applyresume(id, body)` — PUT /technical-datas/{id}/applyresume — Update technical data's by resume
- `download(id)` — GET /technical-datas/{id}/download — Get technical data's formatted file content

## client.api.threads (/threads)

- `search()` — GET /threads — Search threads
- `create(body)` — POST /threads — Create a thread
- `default(params={typeOf*})` — GET /threads/default — Get empty thread's default basic data
- `delete(id)` — DELETE /threads/{id} — Delete thread
- `get(id)` — GET /threads/{id} — Get thread's basic data
- `update(id, body)` — PUT /threads/{id} — Update thread

## client.api.thumbnails (/thumbnails)

- `create(body)` — POST /thumbnails — Create a thumbnail
- `delete(id)` — DELETE /thumbnails/{id} — Delete the thumbnail
- `get(id)` — GET /thumbnails/{id} — Get thumbnail

## client.api.times (/times)

- `search()` — GET /times — Search times

## client.api.times_reports (/times-reports)

- `search(params={startMonth*, endMonth*})` — GET /times-reports — Search timesheets
- `create(body)` — POST /times-reports — Create a timesheet
- `default(params={resource*, term*})` — GET /times-reports/default — Get empty timesheet's default basic data
- `delete(id)` — DELETE /times-reports/{id} — Delete the timesheet
- `get(id)` — GET /times-reports/{id} — Get timesheet's basic data
- `update(id, body)` — PUT /times-reports/{id} — Update basic data related to a timesheet
- `download(id, params={type*})` — GET /times-reports/{id}/download — Get timesheet formatted file content
- `reject(id, body, params={expectedValidator*, reason*, rejectTypeOf*})` — POST /times-reports/{id}/reject — Reject a timesheet
- `rights(id)` — GET /times-reports/{id}/rights — Get timesheet's rights
- `signature(id, body, params={type*, mailValidatorSignature*})` — POST /times-reports/{id}/signature — Create/update signature data related to a timesheet
- `unvalidate(id, body, params={expectedValidator*})` — POST /times-reports/{id}/unvalidate — Unvalidate a timesheet
- `validate(id, body, params={expectedValidator*})` — POST /times-reports/{id}/validate — Validate a timesheet

## client.api.todolists (/todolists)

- `search()` — GET /todolists — Search TodoLists
- `create(body)` — POST /todolists — Create a TodoLists
- `delete(id)` — DELETE /todolists/{id} — Delete the TodoList
- `get(id)` — GET /todolists/{id} — Get TodoList's data
- `update(id, body)` — PUT /todolists/{id} — Update data related to a TodoList.

## client.api.trustelem (/trustelem)

- `delete(id)` — DELETE /trustelem/{id} — Log out user

## client.api.validations (/validations)

- `search(params={startMonth*, endMonth*})` — GET /validations — Search validations
- `create(body)` — POST /validations — Create validations alert calculation
- `delete(id)` — DELETE /validations/{id} — Delete the validation
- `get(id)` — GET /validations/{id} — Get validation's basic data
- `update(id, body)` — PUT /validations/{id} — Update basic data related to a validation

## client.api.vendor (/vendor)

- `search()` — GET /vendor — Get vendor's basic data
- `update_many(body)` — PUT /vendor — Update basic data related to a vendor
- `delete_logo()` — DELETE /vendor/logo — Delete the logo
- `update_logo(body)` — PUT /vendor/logo — Update logo

## client.api.webhooks (/webhooks)

- `search()` — GET /webhooks — Search webhooks
- `create(body)` — POST /webhooks — Create a request of webhook
- `delete(id)` — DELETE /webhooks/{id} — Delete the webhook
- `get(id)` — GET /webhooks/{id} — Get webhook
- `update(id, body)` — PUT /webhooks/{id} — Update webhook data

## client.api.workplaces_times (/workplaces-times)

- `search()` — GET /workplaces-times — Search workplace's times
