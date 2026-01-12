## Task1

* `Step1 Download Data.ipynb`: code for downloading data from the messaging platform.
* `Step2 Annotator Agreement.ipynb`: code for calculating IAA.
* `Step3 Validate UserIds.ipynb`: code for validating and re-annotating user ids (manually).
* `raw_data/rooms.jsonl`: list of chat room in the platform created by participants.
* `raw_data/conversations.jsonl`: list of raw conversations in the platform created by participants.
* `raw_data/task1_labels.csv`: annotated labels
* `raw_data/topics.csv`: seeding topics
* `raw_data/re_annotated_user_ids.json`: user ids that needed to re-map to other user id 
* `raw_data/validated_labels.csv`: labels at the validation step

#### Note
During data collection, some participants were disconnected and reconnected to the messaging platform multiple times, resulting in new user IDs being assigned upon each re-entry. As a result, some chat rooms contained multiple user IDs corresponding to the same individual. To resolve this, the researchers manually reviewed and reassigned user IDs based on the conversational context, ensuring that the dialogue flow remained coherent and that each conversation involved only two unique participants.


#### Please ignore
* `deprecated/task1_validating.jsonl`: data sent to Wang.in.th in the validation step
