# Announce Bitcoin Price
In this program first with api from [API Ninjas](https://api-ninjas.com/api/bitcoin#bitcoin-endpoint) it will get **Bitcoin price** then with TTS library in python, it will ***announce price of bitcoin***.

## Setups
+ Login and Get your api-key form [API Ninjas](https://api-ninjas.com/api/bitcoin#bitcoin-endpoint). `It's Free 🆓`
## Python Depedencies

+ Create virtual environment:

```bash
    python -m venv env
```
### Activate virtual environment
+ Mac/Linux
```bash
    source env/bin/activate
```
+ Windows and other
<div class="responsive-table__container"><table class="docutils align-default">
<thead>
<tr class="row-odd"><th class="head"><p>Platform</p></th>
<th class="head"><p>Shell</p></th>
<th class="head"><p>Command to activate virtual environment</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="4"><p>POSIX</p></td>
<td><p>bash/zsh</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <span class="pre">source</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/activate</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>fish</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <span class="pre">source</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/activate.fish</span></code></p></td>
</tr>
<tr class="row-even"><td><p>csh/tcsh</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <span class="pre">source</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/activate.csh</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>pwsh</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/Activate.ps1</span></code></p></td>
</tr>
<tr class="row-even"><td rowspan="2"><p>Windows</p></td>
<td><p>cmd.exe</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">C:\&gt;</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">\Scripts\activate.bat</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>PowerShell</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">PS</span> <span class="pre">C:\&gt;</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">\Scripts\Activate.ps1</span></code></p></td>
</tr>
</tbody>
</table></div>

+ Install the following python modules into your virtual environment using PIP:

```bash
pip install -r requirements.txt
```
+ Run program. After change directory to announce-bitcoin-price enter code below:
```bash
python main.py
```
`Enter your api key`
