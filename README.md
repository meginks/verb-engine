# verb-engine
This will be an attempt to derive and compare the rules for conjugating verbs in Spanish, French, Italian and Portuguese using Python in a simple, declarative and human-readable-but-in-code way.

I started these verb conjugators in separate repositories for each of the following languages, but have since combined them into one here. 
 
- Spanish 
- French
- Portuguese
- Italian 

I attempt to cover all the tenses -- the 7 simple and 7 compound tenses plus imperative that occur across these Romance languages and the additional tenses that exist only within Portuguese (for example, the personal infinitive). 

 This is ultimately a self-education project with the goal of internalizing these rules through the medium of code and to increase my fluency in these languages by looking at their similarities and differences grammatically. If it helps anyone else make sense of the verbs in these languages, that's great. Full disclaimer though that I am neither a linguist nor an expert, and there may be mistakes. If you find any, please let me know. I obviously don't own the Spanish, French, Italian, or Portuguese languages, and I did not come up with these rules of conjugation, but I did write all the Python.   

 I started this project with the Spanish language, using the system for conjugating Spanish verbs that Dr. Eric Vogt lays out in the book Spanish Irregular Verbs Up Close of the McGraw Hill series Practice Makes Perfect. This project, which started in only Spanish, is an attempt to codify those rules in that system into Python so that one can generate the verb conjugations from inserting the infinitive form in Spanish, French, Italian, and Portuguese. 
 
 This is intentionally done without the use of any AI and is relying on pure logic representing the conjugation rules and reference data containing 6 forms of each verb -- first person singular present, second person singular present, the infinitive, first person singular preterite, gerund and past participle. In Portuguese, multiple forms of the past participle are stored. While it might be easier from a coding perspective, to use something like regular expressions, I have chosen not to do that one goal with this is for it to be easy for a person to read and understand.

I have created this project as a way to help myself understand verbs in these Romance languages better, but I have made it public in the event that thinking about it in this way is useful to anyone else who is learning any of them. If you find an issue with it, please let me know. 

 ## References 

- Vogt, Eric. Practice Makes Perfect: Spanish Irregular Verbs Up Close.  
- Colaneri, John and Vincent Luciani (2001). 501 Italian Verbs.
- Kendris, Christopher (1990). 501 French Verbs. 
- Kendris, Christopher, and Theodore Kendris (2020). 501 Spanish Verbs.
- Nitti, John and Michael Ferreira (1995). 501 Portuguese Verbs.
