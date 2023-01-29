def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "hey, How's its going?"
    
    if user_message in ("who are you", "who are you?", "what do you do", "what do you do?"):
        return "I am Hackathon  adviser bot. I will guide you in how to ace in hackathons, will provide materials and will inform you about latest happenning hackathons. "

    if user_message in ("what are hackathons?", "what is hackathon?", "what are hackathons", "what is hackathon", "hackathon", "hackathons", "hackathon?", "hackathons?"):
        return "A hackathon is an event where developers, designers, innovators, data scientists, and other domain experts get together for a sprint-like event to collaborate on intense projects to solve specific problems. Hackathons can last anywhere from 24 to 48 hours depending on the expected outcome."
    
    if user_message in ("basic requirement to participate in hackathon", "can i participate in hackathon", "am i eligible for hackathon", "eligibility"):
        return "eligibility criteria vary from hackathon to hackathon. Please refer to the hackathon website you are targetting to know about it"

    if user_message in ("skills", "skills required for hackathon", "basic skills", "basic skills required for hackathons"):
        return "Creativity is the main skill required. The techstacks can be learned in a day to fulfill the rquirement of hackathon although it is advisable to be thorough with atleast one techstack so as to handle that particular part of the project."

    if user_message in ("benifits", "benifits of participating in hackathons", "what are the benifits of participating in hackathon"):
        return """
         A hackathon has plenty of benefits, which I plan to discuss below.

Networking. At a hackathon event, you will usually meet people who have the same interests and skills as you. This creates the perfect environment for networking. All you need to do is network and exchange contact information with your fellow coders. Who knows, you may end up collaborating in the future.

Add value to your resume or CV. Hackathon participation looks very good on your resume or CV. It signals to people that you have programming skills, experience working in intense environments, and know how to win. People know that participating in a hackathon instantly increases your knowledge and skill level.

Create new concepts and ideas. Intense problem-solving environments like hackathons facilitate the creation of innovative ideas and concepts. You must work with people from various fields, with multiple interests and skills, all collaborating to solve the same problem. The fact that there are time constraints make the task more exciting and brings out the best in people.

Company branding. If your company sponsors or organizes a hackathon, it can instantly increase its name recognition in its industry. The people who attend the event will become intimately acquainted with your company and its employees. That way they start to understand how your team operates and what you bring to the table.

Talent Acquisition. If your company organizes or sponsors the project, you can use this opportunity to assess and identify potential talent. If they can produce in this intense, fast-paced environment, odds are they will able to produce at an elevated level at your company. This makes hackathons an excellent way for tech companies to find talent.

Product development. The main idea behind a hackathon is to identify a problem and work collaboratively to create technologies that solve that problem. At the end of the hackathon, companies find that they have one or more prototypes, which could become new products."""


    if user_message in ("should i participate in hackathons"):
        return "Yes, if you fulfill the age limit criteria, you should definitely participate in hackathons."

    return "Please be more specific with your text or command"
