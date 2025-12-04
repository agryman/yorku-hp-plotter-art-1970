# York University HP Plotter Art, 1970
*Arthur Ryman, arthur.ryman@torontomu.ca, 2025-12-04*

## Background

On 2024-10-26 I received the following email from Zbigniew Stachniak:
> I'm a senior scholar at York University and the curator of York University Computer Museum.
I'm writing to you hoping that you are the Arthur Ryman who, as physics student at York U 
in the early 1970s, was involved with plotter art, publishing some of the artwork on the
covers of York's Computer Centre Users' Newsletter. 

He sent me the following image:

![Newsletter Cover](scanned-images/1971-04-28-York-University-Computer-Services-Users-Newsletter-Cover.jpg)

Yes, that was me. 
While attending York University as a B.Sc. student, 1969-1972, 
I created some mathematical artwork which ended up on the covers of several
issues of the university's Computer Services Users' Newsletter.

Zbigniew was researching the history of computing at York U. during the 
period 1965-1980. His museum was also planning an exhibit of some 
very impressive CalComp plotter art created by another York student,
Will Anielewicz, who went on to become a professional computer
animator.

Zbigniew asked if I had kept any of my original plots.
I vaguely recalled having a file folder but couldn't locate it.
Many months later while decluttering 
I did in fact locate a folder full of the originals and
arranged to drop them off. 
I visited Zbigniew (aka Ziggy), 
on 2025-11-25 and got a fascinating tour of the
museum storerooms and exhibits.
I rambled on about my undergrad days at York 
and how my plotter art came to be.
Ziggy asked me to contribute my memories to the newly-added 
[Narratives](https://museum.eecs.yorku.ca/narratives)
section of the 
[York University Computer Museum](https://museum.eecs.yorku.ca/) website.
This article gives my recollection of how and why I created the artwork,
and how it ended up on the newsletter covers.

## Q & A

**Q:** Let me start by asking about your early experiments with plotter art. How did it start and when 
(to the best of my knowledge, 
the first of your artwork appeared in 1971 in the Computer Services Users' Newsletter (attached))? 

**A:** I was doing a combined Math & Physics B.Sc.
One day while walking around the Math department, probably in 1970, I noticed a new toy in
one of the rooms. It was an 
[HP 9125A plotter](https://hpmuseum.net/display_item.php?hw=82) 
attached to an 
[HP 9100A programmable calculator](https://hpmuseum.net/display_item.php?hw=50).
I had learned FORTRAN programming at my high school, Northview Heights, and also APL at York.
Northview had its own IBM 1130 minicomputer connected to a line printer.
York APL ran from dial-up IBM Selectric typewriter terminals. 
I had tried to produce text-based mathematical plots
on both systems but the results were not great. 
The HP plotter was the first device that I had access to that
could actually produce high-resolution graphical output.

The HP 9100A was programmable but had very little memory.
I therefore needed to select a relatively simple mathematical curve that would produce a visually interesting result.
I decided to plot Lissajou figures. 
I had previously produced them on oscilloscopes at high school.
They are the curves you see on oscilloscopes in science fiction movies when the scene takes place in a lab.

I coded a simple Lissajou figure.
My program simply computed the curve at a series of points and connected then with straight lines.
I then ran the program.
The result should have been a nice smooth curve, like the following:

![Smooth Curve](plots/delta-1.png)

However, my first plot looked like string art because I had a configuration error:

![Smooth Curve](plots/delta-113.png)

A Lissajou figure is defined using trigonometric functions.
The HP calculator had a setting that affected the interpretation of arguments to trig functions.
You could select either degrees or radians. The default setting was radians but my program assumed degrees.
My program incremented the curve parameter by one, which would have resulted in a smooth curve had the setting been
degrees. However, one radian is around 57 degrees so successive points on the curve were very far apart
resulting in long straight lines connecting distant points.
Although the result was not what I expected, I thought it actually looked more interesting.
The long line segments looked like they formed a ruled surface and
new parallel curves emerged from where they intersected.

Over that next few days I tried various Lissajou figures and parameter value increments.
I also programmed some simple curves defined using polar coordinates.
These looked like rosettes.
Some of the plots were very visually interesting.
I pinned them on the walls.

**Q:** How did your work find its way onto the covers of the newsletter? 

**A:**  I didn't submit my plots. I didn't even know that the newsletter existed.
I assume that one of the grad students or professors came into the plotter room,
saw the plots pinned to the walls, and thought they would make nice newsletter covers.
I recall that some of my plots occasionally disappeared, 
but thought someone was simple cleaning up the room.
However, one day someone handed me a folder of my missing plots.
I filed them away.

**Q:** Were there other people who you were collaborating with? 

**A:** I didn't directly collaborate with anyone but I do remember getting some very positive
feedback from one of the grad students. He said that one of the plots looked like a double Klein bottle.
He brought in one of the math profs, Richard Brown I believe, who I think was a topologist.

**Q:** Did you do any plotter art (or, in general, any computer art) after graduation from York?

**A:** No. I don't regard myself as an artist. I do appreciate good visualizations of mathematical objects.
I think mathematical objects often have intrinsic beauty.
I believe that good visualizations should present them accurately.
I wouldn't take artistic licence to alter the faithfulness of a mathematical visualization simply to make it look better.

**Q:** In the 1960s, digital computers were not a common sight in Canadian high schools. 
What do you remember about the use of the IBM 1130 at Northview Heights? 

**A:** You are certainly correct.
I entered Northview Heights in 1966 and was delighted to see a brand new IBM 1130
sitting in a deserted machine room, along with a punched card reader and line printer.
The adjoining room had a half dozen card punch machines. 

Computers were so novel back then that programming was not yet part of the curriculum.
However, there was a notice posted on the machine room door advertising that Mr. Wong, 
one of the teachers, would be giving programming classes after school.
I showed up and learned FORTRAN.

I didn't know it at the time, but I was extremely lucky to have access to a real computer
in high school. After you reconnected me with Will, he and I discussed our careers, 
and it turned
out that Will had also attended Northview Heights, but a couple of years after me. 
Will became heavily involved with operating the IBM 1130. 
He told me that one of his friends, a Williams, had
claimed that Northview was actually the first high school in Canada to get a computer for 
instructional use. 

I was a little skeptical of the claim, so I did a Web search and found clear
evidence. 
The report
[Significant developments in local school systems - Ontario's Educative Society, Volume VI
](https://utppublishing.com/doi/book/10.3138/9781487598655)
by W.G. Fleming, published by the University of Toronto Press in 1972,
contains the following text beginning on p. 58:

> COMPUTER SCIENCE
> 
> North York school system
>
>The North York educational system won recognition in the late 1960s
for offering computer courses as comprehensive and effective as those of
any other system in the world.
> 
> ...
> 
> Conspicuous contributions were made by John Del Grande, Co-ordinator
of Mathematics, and Norman E. Williams, Superintendent of Computer
Services.
> 
> ...
> 
> In the spring of 1966 the first computer installed in a secondary school
in Canada for instructional purposes only, an IBM model 1130, began
operations at Northview Heights Secondary School.

It seems highly likely that Will's friend was the son of the Superintendent of Computer Systems.

**Q:** Was computing on this machine a popular activity among your high school peers?

**A:** At that time Ontario had three high school streams: 
Arts & Science, Business & Commerce, and Science, Technology, & Trades. 
Northview was unusual in that it offered all three streams. 
My local high did not offer the ST&T stream but that was what I wanted to take, 
so I had to travel out of my district in order to attend Northview. 
Probably less than one third of the Northview students were in the ST&T stream.
Of those, most were more interested in cars than computers. 
So only a handful of students became computer geeks. 
Remember that this was well before personal computers.

Another of my friends, David Vaskevitch, became an ubergeek at Northview.
He'd often be seen walking the halls carrying a long box of punched cards under his arm.
If I had a programming question, I'd ask David.
Later, David started his own software company and eventually joined Microsoft where
he served as the Chief Technology Officer for many years.

**Q:** Were there any special initiatives, 
such as a computer club or events organized to teach students about computing?

**A:** As I mentioned, computer programming was not even on the curriculum in 1966.
The only computing special initiative that I was aware of was the extracurricular programming class
taught by Mr. Wong.

I'd like to take this opportunity to express my gratitude to Mr. Wong for taking the time
to teach us how to program. It had a big impact on my career.
I managed to find the following picture of Mr. R. Wong in the 1964 Northview Heights Yearbook
which had been posted to a Facebook group.

![Mr. R. Wong, 1964](images/1964-Northview-Heights-Yearbook-Mr-R-Wong.png)

Thank you, Mr. Wong!

That being said, I do recall a couple of other math and science special initiatives.
On two occasions we had school-wide guest mathematics lectures by university professors -
one on calculus by W.W. Sawyer from U. of Toronto, and another on graph theory by
Ross Honsberger from U. of Waterloo. Also, Northview hosted the North York Honours
Science and Mathematics Scholarship Program which I attended in the summer of 1968.
All of these events had a big influence on me. Northview was a very enriching environment.
I was fortunate to attend it.

