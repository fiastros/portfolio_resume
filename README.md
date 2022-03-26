# Portfolio Webapp Install and Launch

## Setup & installation

Be sure that you have at least python3 ( I'm running on python 3.9.2) installed on your system.
Next step is download this repository on your local computer. 
<ol>
<li> On Linux/Mac open the terminal and do the command: 

```bash
git clone https://github.com/fiastros/portfolio_resume
```
</li>


<li>Second step is installing all the needed python libraries to run the program. 
<br> In a terminal (Linux/Mac) type : replace with the pip you have (pip or pip3)

```bash
pip3 install -r requirements.txt  pip install -r requirements.txt
```
</li>

<li>
Third step: rename the file "confidential_example.json" into "confidential.json"
open the file "confidential.json" and replace with your personal gmail 
informations (name, email, email-password). <br>
You must have a gmail account. 
</li>

<li>
fourth step,  this applies only if you want the email features.
<br> Make sure: 
<ul>
<li>Your gmail account should not have the two step verification. </li>
<li>If you account has two step verification then use another account (spam account) which 
does not have two step verification </li>
<li>use this link to authorize google: 
<a  href="https://www.google.com/settings/security/lesssecureapps">Click</a> </li>
<li>Unfortunaly this feature of google will cease to work form May 31 , 2022. <br>
So I'll have to find an alternative.</li>
</ul>

</li>

<li>
fifth step, you can now launch the app: 
from a terminal (Linux/Mac) type: replce "pip" with what you have on your computer 
(pip or pip3)

```bash
python3 run.py  ou python run.py
```
</li>
</ol>

## To access the site

Once the server is running localy, you can access it : 
- Open a browser (Chrome, Firefox...)
- Enter the following url : http://127.0.0.1:5000

For any question, feel free to make a request in the ISSUE section.

## Ongoing work and further improvements

Currently (at the time of writing ): 
- I'm making the back-end of the website 
using 100% Python. 
- Next step will be to host this website on my raspberry pi so that 
Anyone could access it online from anywhere. 

