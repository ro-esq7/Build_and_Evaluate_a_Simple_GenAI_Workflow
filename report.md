# Business Workflow & Task Definition


## The Workflow
For this assignment, I chose a **business writing workflow** focused on drafting warm, professional business emails from rough notes. This is a realistic and valuable task because many professionals often begin with incomplete thoughts, bullet points, or overly casual drafts that need to be rewritten before they are ready to send.

## Users
The **primary user for this workflow is a working professional, such as a manager, analyst, or team lead**, who regularly communicates with colleagues, clients, or partners through email. In fast-paced work environments, these users may not always have the time to carefully refine tone, structure, and clarity on their own.

## System Input
The **system receives a rough input in the form of short notes, bullet points, or an unpolished draft email**. These inputs may include the main message, context, questions, requests, or a desired tone. Based on that input, the system produces a polished email draft that is clearer, more organized, and more professional in tone, while still preserving the user’s original intent.

## Business Value
This task is valuable enough to automate, or at least partially automate, **because email writing is a frequent and repetitive part of business communication**. A GenAI workflow can help save time, improve consistency, and reduce the effort required to turn rough ideas into usable drafts. At the same time, this is still a workflow that benefits from human review, since the sender may need to confirm tone, accuracy, context, and appropriateness before sending the final message.

## Model Choice
For this prototype, I used Google’s Gemini API in Python. I initially selected the **gemini-2.5-flash** model because it seemed like a strong fit for a lightweight text-generation workflow. However, during testing, that model repeatedly returned temporary “high demand” errors, which prevented the prototype from running. To complete the assignment, I switched to **gemini-2.5-flash-lite**, which ran more reliably and still produced strong results for this email drafting task.

I chose **gemini-2.5-flash-lite** because it was accessible, fast enough for a simple command-line prototype, and capable of producing polished email drafts from rough drafts/ notes. I did not compare multiple vendors or run a full benchmark across models, since the goal was to build one working GenAI workflow and evaluate it honestly rather than optimize model selection across platforms.


## Baseline vs. Final Comparison
### Baseline Prompt
My baseline prompt instructed the model to rewrite rough notes into a professional, yet friendly, email while preserving meaning, avoiding invented facts, and keeping the message concise. The first version worked reasonably well on simple cases. It produced outputs that were readable, clear, and generally stayed within the details provided.

However, testing showed that the baseline prompt had two main weaknesses. First, some outputs sounded slightly too casual. Second, the model sometimes added formatting assumptions that were not provided in the input, such as subject lines and signature placeholders.

### Prompt Revision Process
I revised the prompt three times based on the outputs from my evaluation set and live test cases.

**Revision 1** focused on tightening tone and reducing unnecessary formatting assumptions. I added more explicit instructions for a polished and professional tone and told the model not to invent names, subject lines, or placeholders. This improved professionalism and control, but some outputs became too stiff.

**Revision 2** focused on making the drafts feel more natural and complete. I added guidance to include a brief greeting and courteous closing when appropriate. This improved readability and reduced the robotic feel, but it also led the model to overcorrect by adding details that were not provided.

**Revision 3** focused on tone matching. Instead of applying the same level of formality to every case, I instructed the model to adapt its tone to the context of the message. This helped the prototype handle both formal business emails and more relaxed internal workplace messages effectively.

### Final Comparison
Compared with the baseline, the final design produced stronger email drafts overall. The later versions were more controlled, more professional, and more readable across normal and edge cases. The best improvements were in tone control, clarity, and overall structure. For example, the system became better at rewriting short and messy notes into complete email drafts without changing the core meaning.

That said, the improvements were not perfect. The final design still showed a tradeoff between sounding natural and staying strictly within the provided details. When the model was pushed to sound more complete, it sometimes became too assumptive by adding subject lines, signatures, or placeholder names. This means prompt iteration improved the prototype, but did not eliminate the need for human review.


## Failure Cases
The prototype still fails or requires human review in several situations. First, it may overcorrect the tone. Some drafts that should remain friendly and lightweight, such as social or internal workplace emails, became too formal. Second, the model occasionally added structural elements that were not requested, such as subject lines or placeholder signatures. Third, sensitive emails remain risky. If the input involves blame, missing facts, client performance, or any situation where wording could have business consequences, the model should not be trusted to produce a final send-ready draft without review.

This was especially important in the human-review test case, where the input asked for an email about campaign underperformance and suggested adding numbers “if needed.” In a case like that, the model must not invent performance data or make unsupported claims. Even if the tone is polished, the user still needs to verify facts, wording, and business appropriateness before sending anything externally.


## Deployment Recommendation
I would recommend deploying this workflow only as a draft-generation assistant, not as a fully autonomous email sender. The prototype is useful for speeding up repetitive writing tasks and improving rough drafts, especially for internal business communication or low-risk professional emails. It is strongest when the user already knows the message they want to send and simply needs help polishing it.

I would not recommend deploying this workflow without review controls. At minimum, the system should require a human to check tone, confirm factual accuracy, and remove or adjust any invented formatting details before sending. For higher-risk use cases, especially client-facing, sensitive, or performance-related messages, human approval should be mandatory. Overall, I believe this workflow is helpful as a productivity tool, but not reliable enough to replace human judgment.