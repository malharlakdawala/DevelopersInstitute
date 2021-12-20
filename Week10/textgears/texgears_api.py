import requests

URL = "https://api.textgears.com/suggest"
Text = "Manufacturers and exporters of orthopaedics softgoods. <p>Tynor Orthotics P. Ltd. was conceived at a time when orthopedic products available to Indian patients were either very low quality that were produced in India very expansive and not affordable if they were imported. Mid 90's witnessed a major overhaul of the microeconomic fiber of India. With the opening of the economy Indian consumers were exposed to the world class products in almost all fields. Indian consumers were yeaming for world class and affordable products in orthopedics as well.</p>"
PARAMS = {'language': "en-GB", 'key': "j8Ds420eJpEvUsYL", 'text': Text}
r = requests.get(url=URL, params=PARAMS)
print(r.text)

# https://rapidapi.com/smodin/api/rewriter-paraphraser-text-changer-multi-language/pricing
# # https://rapidapi.com/OpenedAI/api/gpt-summarization/
# # https://rapidapi.com/dev.nico/api/ai-powered-content-moderator/
#https://rapidapi.com/translated/api/text-readability/
#https://rapidapi.com/healthytechguy/api/paraphrasing-tool1/pricing ->cheaper
#https://rapidapi.com/microbrands/api/textrewrite-com/ >cheaper
# dearrnbuyerrnwe are making only ladies tops western formal kurtisrnif you are interested to buy it pls reply as soon as possiblernthanks rnregardrnsonali
#
#
# Indian handicrafts as Brass artwaresrnepnswares wood carvingsrnLantern candle stand candle snuffernapkin ring votive flower vase etc
#
#  pestablished in b2006b we ldquobspiktel technologies private limitedbrdquo is engaged manufacturing and supplying wifi wi max vsat coaxial cables fiber optics catv digital head ends analog head ends hfc cas iptv set top boxes dvbc dvbs dvbt and accessories to our clients all across the country and are highly known for its easy installation and economic cost these products are manufactured using highgrade inputs that are sourced from the renowned a
rules, remove below items
\n
\r
<anything inside>
\
multiple ...
Was Established In....(Year) With ....Employees And We Are The ->handle this

first person to third

we, I -> company
us -> they
