import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_soup(start_season, end_season, league, qual, ind):
	url = "http://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg={}&qual={}&type=c,4,5,11,7,8,13,-1,36,37,40,43,44,48,51,-1,6,45,62,-1,59,-1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299&season={}&month=0&season1={}&ind={}&team=&rost=&age=&filter=&players=&page=1_100000"
	url = url.format(league, qual, start_season, end_season, ind)
	s=requests.get(url).content
	#print(s)
	return BeautifulSoup(s, "html.parser")

def get_table(soup):
	#doesn't work yet
	tables = soup.find_all('table')
	table = tables[10]
	data = []
	# couldn't find these in the table, hardcoding for now
	headings = ["Name","Team","W","L","SV","G","GS","IP","K/9","BB/9","HR/9","BABIP","LOB%","GB%","HR/FB","ERA","FIP","xFIP","WAR","Age","W","L","ERA","G","GS","CG","ShO","SV","BS","IP","TBF","H","R","ER","HR","BB","IBB","HBP","WP","BK","SO","GB","FB","LD","IFFB","Balls","Strikes","Pitches","RS","IFH","BU","BUH","K/9","BB/9","K/BB","H/9","HR/9","AVG","WHIP","BABIP","LOB%","FIP","GB/FB","LD%","GB%","FB%","IFFB%","HR/FB","IFH%","BUH%","Starting","Start-IP","Relieving","Relief-IP","RAR","WAR","Dollars","tERA","xFIP","WPA","-WPA","+WPA","RE24","REW","pLI","inLI","gmLI","exLI","Pulls","WPA/LI","Clutch","FB%","FBv","SL%","SLv","CT%","CTv","CB%","CBv","CH%","CHv","SF%","SFv","KN%","KNv","XX%","PO%","wFB","wSL","wCT","wCB","wCH","wSF","wKN","wFB/C","wSL/C","wCT/C","wCB/C","wCH/C","wSF/C","wKN/C","O-Swing%","Z-Swing%","Swing%","O-Contact%","Z-Contact%","Contact%","Zone%","F-Strike%","SwStr%","HLD","SD","MD","ERA-","FIP-","xFIP-","K%","BB%","SIERA","RS/9","E-F","FA% (pfx)","FT% (pfx)","FC% (pfx)","FS% (pfx)","FO% (pfx)","SI% (pfx)","SL% (pfx)","CU% (pfx)","KC% (pfx)","EP% (pfx)","CH% (pfx)","SC% (pfx)","KN% (pfx)","UN% (pfx)","vFA (pfx)","vFT (pfx)","vFC (pfx)","vFS (pfx)","vFO (pfx)","vSI (pfx)","vSL (pfx)","vCU (pfx)","vKC (pfx)","vEP (pfx)","vCH (pfx)","vSC (pfx)","vKN (pfx)","FA-X (pfx)","FT-X (pfx)","FC-X (pfx)","FS-X (pfx)","FO-X (pfx)","SI-X (pfx)","SL-X (pfx)","CU-X (pfx)","KC-X (pfx)","EP-X (pfx)","CH-X (pfx)","SC-X (pfx)","KN-X (pfx)","FA-Z (pfx)","FT-Z (pfx)","FC-Z (pfx)","FS-Z (pfx)","FO-Z (pfx)","SI-Z (pfx)","SL-Z (pfx)","CU-Z (pfx)","KC-Z (pfx)","EP-Z (pfx)","CH-Z (pfx)","SC-Z (pfx)","KN-Z (pfx)","wFA (pfx)","wFT (pfx)","wFC (pfx)","wFS (pfx)","wFO (pfx)","wSI (pfx)","wSL (pfx)","wCU (pfx)","wKC (pfx)","wEP (pfx)","wCH (pfx)","wSC (pfx)","wKN (pfx)","wFA/C (pfx)","wFT/C (pfx)","wFC/C (pfx)","wFS/C (pfx)","wFO/C (pfx)","wSI/C (pfx)","wSL/C (pfx)","wCU/C (pfx)","wKC/C (pfx)","wEP/C (pfx)","wCH/C (pfx)","wSC/C (pfx)","wKN/C (pfx)","O-Swing% (pfx)","Z-Swing% (pfx)","Swing% (pfx)","O-Contact% (pfx)","Z-Contact% (pfx)","Contact% (pfx)","Zone% (pfx)","Pace","RA9-WAR","BIP-Wins","LOB-Wins","FDP-Wins","Age Rng","K-BB%","Pull%","Cent%","Oppo%","Soft%","Med%","Hard%","kwERA","TTO%","CH% (pi)","CS% (pi)","CU% (pi)","FA% (pi)","FC% (pi)","FS% (pi)","KN% (pi)","SB% (pi)","SI% (pi)","SL% (pi)","XX% (pi)","vCH (pi)","vCS (pi)","vCU (pi)","vFA (pi)","vFC (pi)","vFS (pi)","vKN (pi)","vSB (pi)","vSI (pi)","vSL (pi)","vXX (pi)","CH-X (pi)","CS-X (pi)","CU-X (pi)","FA-X (pi)","FC-X (pi)","FS-X (pi)","KN-X (pi)","SB-X (pi)","SI-X (pi)","SL-X (pi)","XX-X (pi)","CH-Z (pi)","CS-Z (pi)","CU-Z (pi)","FA-Z (pi)","FC-Z (pi)","FS-Z (pi)","KN-Z (pi)","SB-Z (pi)","SI-Z (pi)","SL-Z (pi)","XX-Z (pi)","wCH (pi)","wCS (pi)","wCU (pi)","wFA (pi)","wFC (pi)","wFS (pi)","wKN (pi)","wSB (pi)","wSI (pi)","wSL (pi)","wXX (pi)","wCH/C (pi)","wCS/C (pi)","wCU/C (pi)","wFA/C (pi)","wFC/C (pi)","wFS/C (pi)","wKN/C (pi)","wSB/C (pi)","wSI/C (pi)","wSL/C (pi)","wXX/C (pi)","O-Swing% (pi)","Z-Swing% (pi)","Swing% (pi)","O-Contact% (pi)","Z-Contact% (pi)","Contact% (pi)","Zone% (pi)","Pace (pi)"]
	data.append(headings)
	table_body = table.find('tbody')
	rows = table_body.find_all('tr')
	for row in rows:
	    cols = row.find_all('td')
	    cols = [ele.text.strip() for ele in cols]
	    data.append([ele for ele in cols[1:]])
	data = pd.DataFrame(data)
	data = data.rename(columns=data.iloc[0])
	data = data.reindex(data.index.drop(0))
	return data

def pitching_leaders(season, league='all', qual='y', ind=0):
	soup = get_soup(start_season=season, end_season=season, league=league, qual=qual, ind=ind)
	table = get_table(soup)
	return table


#def get_batting_leaders_range(start_season, end_season, league='all', qual='y', ind=0):
#	pass
