# Elon Musk: frameworks

Pillar: first principles and bureaucracy removal.
Core question: which requirement is real, which step can be deleted, and what is the true constraint?

Source notes. S009, S010 and S011 are three third-party transcriptions of one Starbase tour talk (July 2021). Their wording differs. S012 and S013 are articles; only words they quote from him count as his. Writer paraphrase is labeled (writer's account, S0xx). His DOGE figures in S008 are his own projections, not verified results.

---

## 1. The five-step algorithm

He gives five steps and says the order matters. He admits he has run them backwards himself. The steps are: make requirements less dumb, delete, simplify or optimize, accelerate, automate. Below, each step shows the transcription variants side by side.

**Step 1. Make the requirements less dumb.**
- "Just make your requirements less dumb." [S010]
- "The requirements are definitely dumb; it does not matter who gave them to you." [S011]
- "It's particularly dangerous if a smart person gave you the requirements. You might not question them enough." [S010]
- "It's particularly dangerous when they come from an intelligent person, as you may not question them enough." [S009]
- "No matter who you are, everyone is wrong some of the time." [S011]
- "All designs are wrong, it's just a matter of how wrong." [S011]
- Lower confidence. S009 says it condenses an earlier summary, and S012 gives the same idea as paraphrase. Treat this as possibly condensed: "each required part and process must come from a name, not a department, as a department cannot be asked why a requirement exists, but a person can" [S009]

**Step 2. Delete the part or process.**
- "Then, try very hard to delete the part or process. This is actually very important." [S010]
- "If you're not patiently adding things back in, you're not deleting enough." [S010]
- "If parts are not being added back into the design at least 10% of the time" [S011]
- The 10% benchmark appears in S009 and S011. S010 has no number.
- "The bias tends to be very strongly towards, 'Let's add this part or process step in case we need it.' But you can basically make 'in case' arguments for so many things." [S010]

**Step 3. Simplify or optimize, only third.**
- "Only the third step is simplify or optimize" [S010]
- "The reason this is the third step and not the first step is because the most common error of a smart engineer is to optimize something that should simply not exist" [S011]
- Variant: "The most common error of a smart engineer is to optimize a thing that should not exist" [S010]

**Step 4. Accelerate cycle time, only after steps 1 to 3.**
- "The fourth step is to accelerate cycle time. You're moving too slowly. Go faster. But don't go faster until you've worked on the other three things first." [S010]
- Variant: "You're moving too slowly, go faster! But don't go faster until you've worked on the other three things first" [S011]
- "Because if you are digging your grave, you don't want to dig faster. You want to stop digging your grave." [S011]
- Shorter variant: "If you're digging your grave, don't dig it faster." [S009]

**Step 5. Automate, last.**
- "And then the final step is automate." [S010]
- Lower confidence, same S009 caveat as above: "An important part of this is to remove in-process testing after the problems have been diagnosed" [S009]
- Lower confidence: "if a product is reaching the end of a production line with a high acceptance rate, there is no need for in-process testing." [S009]

**His own mistake, three renderings.**
- "I literally automated, accelerated, simplified and then deleted" [S009]
- "I automated, simplified and then deleted." [S011]
- "Multiple times I automated, accelerated, simplified, and then deleted." [S010]
- "I have personally made the mistake of going backward on all five steps multiple times." [S011]

Applied examples (writer's account, S012): a stage separation pusher system was removed in favor of rotation; dedicated thrusters were replaced by venting gas; grid fins stopped folding because folding adds mass and failure modes; work not needed for the first orbital test was deferred.

Council use: before funding a new hospital process, ask who by name owns each requirement, then try to delete it before improving it. Automating a broken approval chain only makes it faster (inferred from S009, S010, S011).

---

## 2. First principles versus reasoning by analogy

Analogy means copying others with small changes. He says that is fine for daily life but not for doing something new. For new work, break the problem into fundamental truths and reason up.
- "boil things down to their fundamental truths and reason up from there, as opposed to reasoning by analogy." [S005]
- "Through most of our life, we get through life by reasoning by analogy, which essentially means copying what other people do with slight variations." [S005]
- "And you have to do that. Otherwise, mentally, you wouldn't be able to get through the day." [S005]
- "But when you want to do something new, you have to apply the physics approach." [S005]

---

## 3. Physics is the law; test against reality

He ranks physical limits above man-made rules. A rule made by people can be questioned. A conclusion must still be checked against what actually happens.
- "Like physics is the law, everything else is a recommendation. I've seen plenty of people break the laws made by man, but none break the laws made by physics." [S007]
- "You have to test any conclusions against the ground truth of reality. Reality is the ultimate judge." [S007]

Caution: a line in S007 about the only rules being the laws of physics is Lex Fridman reading the Isaacson biography. It is not Musk's own statement.

---

## 4. Cost-element breakdown

He splits a cost into its parts and attacks each one. He looks for the few drivers that matter and for factors that multiply.
- "Our approach has been to focus on reducing all the cost elements of a launch vehicle company, those being propulsion, structures, avionics, launch operations and general overhead." [S004]
- Raw input versus total: "the cost of the propellant is about .3 percent of the cost of the rocket." [S005]
- Two drivers for solar: "the key thing to do is to get the cost of that initial installation low, and then get the cost of the financing low" [S005]
- Stacked factors for tunnels: "the tunneling cost scales with the cross-sectional area." [S006] and "Combine that and that's a factor of eight." [S006]

Council use: for any hospital line item, list the component costs, find the share each takes, and ask whether the biggest one is a real requirement (inferred from S004, S005, S006).

---

## 5. The limiting factor

He asks what single thing is holding progress back right now. When it is fixed, the constraint moves somewhere else, and he tries to predict where.
- "So at various points, there's some kind of limiting factor to progress and with regard to AI, I'm saying right now the limiting factor is silicon chips" [S007]
- "The initial constraint being literally voltage step down transformers" [S007]
- "I do not think there are multiple problems in space; I think there is one, and that is the cost of access to space." [S003]
- "This problem of affordability dwarfs all others." [S003]
- Regulation can be the constraint: "the limiting factor for SpaceX for Starship launch is regulatory approval" [S007]

---

## 6. Make it work, then make it efficient; the factory is the product

First get something working. Then make it efficient. At scale, he says the production system matters more than the product design.
- "In general, with any given technology, you first try to make it work, and then you make it efficient." [S007]
- "Tesla engineering has transitioned to focus heavily on designing the machine that makes the machine" [S002]
- "turning the factory itself into a product" [S002]

---

## 7. Line-item interrogation: find the defender

Used at DOGE (farewell press conference, 2025-05-30). Go through each spend. Ask what it is for and whether it is used. If no one defends it, stop it. Start with assets that have zero users.
- "It's going through really millions of line items and saying just each one of them makes sense or not make sense." [S008]
- "just really asking questions, what's this money for? Are you sure it's actually being used?" [S008]
- "So for a lot of the expenses, there is actually no defender at all." [S008]
- "if no one's using the software, we can terminate this software license agreement" [S008]

---

## 8. Bureaucracy as complaint minimization

His diagnosis of why waste survives in public bodies (2025-05-30). He blames incentives more than people. Paying is easier than questioning.
- "you can't really even blame the individuals because the way the government works is complaint minimization." [S008]
- "their manager will say, it's not worth the trouble, just pay it anyway. That happens over and over again." [S008]
- Maxim he credits to a thinker he names as Tom Friedman: "money is spent most poorly when it is someone else's money being spent on people you don't know" [S008]

---

## 9. Shortest-path communication and the meeting code

From his 2018 email to Tesla staff, quoted by CNBC. Information should flow directly between whoever needs it. Meetings must earn their time. Rules that are obviously silly should be changed.
- "Communication should travel via the shortest path necessary to get the job done, not through the 'chain of command'." [S013]
- "Excessive meetings are the blight of big companies and almost always get worse over time." [S013]
- "Walk out of a meeting or drop off a call as soon as it is obvious you aren't adding value. It is not rude to leave, it is rude to make someone stay and waste their time." [S013]
- "If following a 'company rule' is obviously ridiculous in a particular situation, such that it would make for a great Dilbert cartoon, then the rule should change." [S013]

---

## 10. Urgency and speed of iteration

He treats speed as a lever on the odds of success. Low-consequence work should iterate fast. Draft first, then refine.
- "if we operate with extreme urgency we have a chance of making life multi-planetary. It's still just a chance, not for sure. If we don't act with extreme urgency, that chance is probably 0." [S012]
- "Create a draft and then you iterate on that draft until it has coherence, until it all adds up basically." [S007]

---

## 11. Prize-in-parallel procurement and fair competition

Testimony to the Senate (2004-05-05) and a joint hearing (2003-07-24). He argued that cost-plus contracts reward failure and favor incumbents. He proposed prizes run in parallel to contracts. He asked for fair, open awards.
- "parallel every major NASA contract award with a prize valued at one tenth of the contract amount." [S003]
- "If another company achieves all of the contract goals first, they receive the prize and the main contract is cancelled." [S003]
- "If you get an estimate, whatever the NASA estimate is to get something done, erase a zero and make that a prize." [S003]
- "Unlike standard contracting, where failure is often perversely rewarded with more money, failure to win a prize costs us nothing." [S003]
- "If you shut down the process of new companies getting into such a market, you won't see the price decrease, you won't see the quality improvement, because there is no forcing function for incumbents to change." [S004]
- "It is critical that the Government acts and is perceived to act fairly in its award of contracts." [S003]

---

## 12. Minimum necessary regulation: his asks of regulators

His 2003 testimony gives a concrete list. One clear authority. Only the burden needed for public safety. Judge the agency by progress it enables. Blanket approvals for routine work. Rewrite rulebooks from zero.
- "there needs to be clear regulatory authority for commercial launch vehicles of all kinds." [S004]
- "providing only the minimum regulatory burden necessary to ensure reasonable safety for the general public." [S004]
- "progress in fostering new launch vehicle developments should be a key metric of success in the performance evaluation of FAA-AST and other federal agencies" [S004]
- "a categorical exclusion, such as exists for airplanes, would be immensely helpful." [S004]
- "the right approach is to do a ground up revision." [S004]

Liability, with his own medical comparison (prepared statement, 2003):
- "One of the surest ways of preventing companies like SpaceX from offering human transportation in the future is to make it an unlimited liability business" [S004]
- "an individual should have the right to waive liability provided the risks are fully explained" [S004]
- "We are seeing a crisis in medical care for similar reasons." [S004]
- He kept an exception: the cap would apply "notwithstanding clearly egregious conduct" [S004]

Later load (2023-11-09): "We're subject to, I think over a hundred regulatory agencies domestically and internationally. It's a lot." [S007]

---

## 13. Risk tiering by consequence

How hard to test depends on what a failure costs. Safety is a matter of probability, not perfection (writer's account, S012): crewed Dragon can never fail; uncrewed Starship can iterate and fail often.
- "Starship does not have anyone on board so we can blow things up. It's really helpful." [S012]
- "The thing to appreciate about vehicle safety is this is probabilistic." [S006]
- "So really the key threshold for autonomy is how much better does autonomy need to be than a person before you can rely on it?" [S006]

---

## 14. Where he concedes safety and regulatory limits

He does not argue for zero regulation. His own words accept a safety floor, a need for oversight in some fields, and the limits of his own cuts and forecasts.
- Safety floor in his core ask: "providing only the minimum regulatory burden necessary to ensure reasonable safety for the general public." [S004]
- AI oversight (2023-11-09): "I've been pushing for some kind of regulatory oversight for a long time." [S007]
- "I think it would be wise for us to have at least an objective third party who can be like a referee" [S007]
- "It's never going to be perfect. No system is going to be perfect" [S006]
- Validation before release: "Every release goes through extensive internal validation before it reaches any customers." [S002]
- Regulators set the pace: "there will still be a significant time gap, varying widely by jurisdiction, before true self-driving is approved by regulators." [S002]
- Procurement humility: "it is possible that NASA has made the right decision in this case." [S003]
- DOGE (2025-05-30): some cuts blamed on DOGE were, in his words, "including things that made no sense and we would agree, made no sense" [S008]
- Timelines: "I would say that I'm pathologically optimistic on schedule. This is true." [S007]

Council use: in a hospital, the patient-safety floor is the equivalent of his reasonable-safety test. Delete process above that floor, not below it (inferred from S004, S006, S007).
