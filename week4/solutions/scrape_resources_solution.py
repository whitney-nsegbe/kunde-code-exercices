#GROUP: Food Security

from pathlib import Path

from  week4.Part_2_APIS_AI.tavily_search import search_link
from week3.Part_3_Prompt.prompt_test import get_answer

resources_links = [
"https://www.ottawatherapygroup.ca/","https://portagetherapygroup.com/","https://www.psychotherapycollective.ca/", "https://ottawa.cmha.ca/"
]
#1
# This is for previewing the results only 
def preview_link_results(links):
    for link in links:
        results = search_link(link)
        print(results)
#3 
RESOURCE_EXTRACTION_PROMPT = """You are an information extraction system.

THE PROVIDED CONTENT IS YOUR ONLY SOURCE OF TRUTH.

Your task is to extract structured information about each organization from the provided cleaned website content.

IMPORTANT:

You MUST NOT use:

* prior knowledge
* general knowledge
* information from the internet
* assumptions
* guesses
* common patterns
* realistic-looking placeholder information
* information from other organizations
* information from previous examples

You may ONLY output information that is explicitly supported by the provided content.

It is ALWAYS better to return "Not found - verify" than to guess or infer.

The JSON structure is ONLY a format for organizing the information. It is NOT a list of fields that must be filled.

CRITICAL SOURCE RULES:

1. Before outputting ANY factual value, verify that the information is explicitly present in the provided content.

2. Every factual value must be traceable to a SOURCE URL included in the provided content.

3. Do not invent organizations, URLs, phone numbers, emails, addresses, hours, languages, costs, eligibility requirements, services, accessibility information, or other details.

4. Do not use information from one organization to fill a field for another organization.

5. Do not assume that information belongs to an organization simply because it appears on that organization's website.

6. If a webpage mentions another organization, program, service, resource, therapist, provider, or external organization, keep that information separate and do not attribute it to the organization hosting the webpage.

7. Do not turn external resources into services provided by the organization.

8. Do not turn general informational statements into organization-specific facts.
   For example, if a page says "family therapy in Ontario typically costs $150-$250 per session," do NOT report $150-$250 as the organization's actual cost unless the source explicitly says that the organization charges that amount.

9. Do not turn program-specific information into organization-wide information.
   For example, if one program is for people aged 16-64, do not state that the entire organization only serves people aged 16-64.

10. Do not turn therapist-specific information into organization-wide information.
    If a language, age group, cost, availability, specialization, or eligibility requirement applies only to a specific therapist, preserve that distinction.

11. Preserve important qualifiers such as:

* "for this program"
* "for qualifying individuals"
* "by referral"
* "on request"
* "varies by therapist"
* "subject to availability"
* "for residents of Ontario"
* "online only"
* "adults 18+"

12. For costs and insurance, be especially strict.
    Do not assume that a service is free, covered by insurance, publicly funded, tax deductible, or reimbursed unless the provided content explicitly supports that claim for the specific organization or service.

13. For languages, only attribute a language to an organization if the provided content explicitly attributes that language to the organization or its specific service. If the language belongs to an external organization or resource, keep it separate.

14. For hours, distinguish between:

* organization-wide hours
* program/service-specific hours
* therapist/provider-specific availability

15. For contact information, distinguish between:

* general organizational contact information
* program-specific phone numbers
* program-specific emails

16. Do not "correct" missing or uncertain information using your own knowledge.

17. If a field is not explicitly supported by the provided content, return exactly:
    "Not found - verify"

18. Never use words such as "likely", "probably", "appears to", "may", or "seems" to fill a missing field.

OUTPUT FORMAT:

Return one JSON object for EACH organization explicitly represented in the provided content.

Use this structure:

[
{
"organization_name": {
"value": "",
"source": ""
},
"website": {
"value": "",
"source": ""
},
"description": {
"value": "",
"source": ""
},
"phone": {
"value": "",
"source": ""
},
"email": {
"value": "",
"source": ""
},
"address": {
"value": "",
"source": ""
},
"hours": {
"value": "",
"source": ""
},
"languages": {
"value": "",
"source": ""
},
"eligibility": {
"value": "",
"source": ""
},
"cost": {
"value": "",
"source": ""
},
"how_to_access": {
"value": "",
"source": ""
},
"requirements": {
"value": "",
"source": ""
},
"services": [
{
"service_name": "",
"description": "",
"source": ""
}
],
"accessibility": {
"value": "",
"source": ""
},
"external_resources": [
{
"name": "",
"description": "",
"source": ""
}
]
}
]

SOURCE REQUIREMENT:

For every field containing actual information, the "source" must be the exact SOURCE URL from the provided content that supports that information.

If the field contains "Not found - verify", set its source to "".

For services, include the source URL where that specific service is supported.

If multiple sources support different parts of the same field, list the relevant information together and include the corresponding source URLs separated by "; ".

Do not create a source URL that was not provided in the content.

ORGANIZATION SEPARATION:

Keep each organization completely separate.

If the provided content contains:

ORGANIZATION A
SOURCE: https://organizationA.com/
...

ORGANIZATION B
SOURCE: https://organizationB.com/
...

do not transfer any information between them.

EXTERNAL RESOURCES:

If an organization mentions another organization or external resource, do not include it under the organization's "services".

Instead, place it under "external_resources".

Only include external resources when they are explicitly mentioned in the provided content.

FINAL CHECK BEFORE RESPONDING:

For EVERY value you are about to output, ask:

"Can I point to the exact provided content and SOURCE URL that supports this?"

If NO:
output "Not found - verify".

If YES:
output the supported information without adding anything.

Return ONLY valid JSON. Do not include explanations, commentary, markdown, or text outside the JSON.

PROVIDE

"""
# ! FIX THIS def extract_resource_info(contents):
#     combined_content = "\n\n--- RESOURCE ---\n\n".join(contents)
#     prompt = f"""{RESOURCE_EXTRACTION_PROMPT}

#     Here is the information gathered from Tavily:
#     {combined_content}
#     """
#     return get_answer(prompt)



#2
resources_content = []
def crawl_resources(links):
    # just for sanity sake
    total_sum_of_char = 0
    for link in links:
        result = search_link(link)
        try:
            for i in result["results"]:
                if i["raw_content"]:
                    resources_content.append(
                        f"url: {i['url']}\ncontent: {i['raw_content']}"
                    )
        except IndexError:
            print(result["failed_results"][0]["error"])
        except TypeError:
            print(f"Could not retrieve resource for: {link}")
    for content in resources_content:
        if content:
            total_sum_of_char += len(content)
    print(f"NUMBER OF CHAR SENT TO AI: {total_sum_of_char}")
    return resources_content




# then for the most advanced explain how u do this
# ^ IMPORT SUPABASE once their thing is valid supabase.table("resources").insert(resource).execute()

CLEANUP_PROMPT = """
Clean and organize the following website content so it can be used later to extract accurate information about the organization.

Your job is ONLY to clean and organize the content. Do NOT summarize, interpret, infer, or add information.

SOURCE ATTRIBUTION IS CRITICAL:

* Preserve the exact source URL for every piece of information whenever possible.
* Every section or group of facts must clearly identify the source URL they came from.
* Do not combine information from different URLs without showing the relevant source URLs.
* If the same information appears on multiple URLs, you may remove the duplicate, but keep at least one source URL.
* If information differs between pages, keep both pieces of information and show the source URL for each.
* Never assign information to a source URL if it did not come from that page.
* If information comes from another organization or external resource mentioned on the page, clearly identify the external organization/resource and preserve the URL where that information appeared.
* Source attribution should make it possible for a later extraction step to trace every important fact back to the original webpage.

Rules:

* Remove navigation menus, headers, footers, cookie notices, privacy notices, terms of service, social media links, newsletter signups, tracking text, repeated buttons, and other website boilerplate.
* Remove duplicated content that appears multiple times across pages.
* Remove irrelevant content such as unrelated blog posts, news articles, job postings, donation requests, and promotional material when it does not provide useful information about the organization or what it offers.
* Keep factual information about the organization, its programs, services, resources, and activities.
* Keep information about who the organization serves, including age, location, residency, income, status, demographics, or other eligibility requirements.
* Keep application, registration, referral, intake, appointment, and enrollment procedures.
* Keep costs, fees, funding, subsidies, coverage, and whether something is free or paid.
* Keep contact information, including phone numbers, email addresses, addresses, websites, contact forms, and other ways to reach the organization.
* Keep hours of operation and service-specific hours.
* Keep locations and service areas.
* Keep languages offered and interpretation options.
* Keep accessibility information and accommodations.
* Keep requirements, documentation, identification, deadlines, waitlists, restrictions, and other conditions.
* Keep information about how to access or use each specific program, service, or resource.
* Keep important limitations or exceptions.
* Keep information that may help someone determine whether a resource is relevant to them.
* Keep qualifiers such as "for this program", "by referral", "for residents of Ottawa", "available online", "appointment required", or "subject to availability."
* If information applies only to a specific program, service, location, staff member, or resource, keep that distinction clear. Do not turn it into an organization-wide claim.
* If the website mentions another organization or an external resource, keep the relevant information but clearly indicate that it belongs to the external organization or resource.
* Do not combine information from different organizations.
* Do not combine information from different programs or services if their details differ.
* Do not guess, fill gaps, or add information that is not present in the source content.
* Do not change the meaning of the original information.
* Do not remove information simply because it seems unusual or unimportant. If it could help someone understand, access, or evaluate the organization's resources, keep it.

Organize the cleaned content into logical sections based on what is actually present. You may use sections such as ABOUT, PROGRAMS, SERVICES, ELIGIBILITY, COST, CONTACT, LOCATION, HOURS, LANGUAGES, ACCESSIBILITY, HOW TO ACCESS, REQUIREMENTS, and OTHER RELEVANT INFORMATION, but do not create empty sections or force information into an inappropriate category.

For every section, clearly include the relevant source URL(s).

Use this structure:

SECTION NAME

SOURCE: [exact URL]

* Cleaned factual information
* Cleaned factual information

SOURCE: [exact URL]

* Cleaned factual information

If several facts come from the same URL, group them together under that URL rather than repeating the URL for every sentence.

The goal is to reduce website noise while preserving as much potentially useful factual information as possible for a later extraction step. The cleaned output should be easy for another AI to read and should allow every important fact to be traced back to its original webpage.

Return only the cleaned and organized content.
--
Treat the cleaned content as source evidence, not as verified organization-level facts. Before assigning a fact to an organization, check its scope and source. Do not turn general informational statements into organization-specific facts. Do not turn therapist-specific, program-specific, service-specific, or external-organization information into organization-wide information. If a cost, eligibility requirement, language, availability, or other detail is only associated with a specific program, therapist, provider, or external organization, preserve that association. If the source does not explicitly support a field, return "Not found - verify" rather than making an inference.

Do not treat general examples, typical industry prices, tax information, insurance explanations, or statements about private practice as the organization's actual pricing or coverage. Only report an organization's specific cost or coverage when the source explicitly attributes it to that organization or service.
"""
if __name__ == "__main__":
    preview_link_results(resources_links)
    results = crawl_resources(resources_links)

    resource_list = "\n".join(resources_links)
    combined_resources = "\n\n---\n\n".join(results)
    final_prompt = f"""
    {CLEANUP_PROMPT}

    The resources are these websites:
    {resource_list}

    Here is the scraped content:

    {combined_resources}
    """
    final_answer = get_answer(final_prompt)

    output_path = Path(__file__).parent / "cleaned_data.txt"
    output_path.write_text(final_answer, encoding="utf-8")

    print(f"Saved output to: {output_path}")