import pandas as pd
import datetime
import re
from markdown import markdown

def to_css(a_time):
	if type(a_time) != str:
		return ""
	if len(a_time) == 4:
		a_time = "0" + a_time.replace(":","")
	else:
		a_time = a_time.replace(":","")
	return a_time

def get_authors(talk):
	authors = ""
	n_speakers = 2
	col_str = "AuthorName{0}"
	aff_str = "AuthorAffil{0}"
	for i in range(n_speakers):
		i += 1
		if not pd.isna(talk[col_str.format(i)]):
			authors += "\n\t\t\t\t" + talk[col_str.format(i)]
			if not pd.isna(talk[aff_str.format(i)]):
				authors += " ({0})".format(talk[aff_str.format(i)])
			authors += "<br>"

	if len(authors) > 0:
		authors = authors[:-4]

	return authors

def make_timeslot(timeslotset, tstart):
	if tstart in timeslotset:
		return ""
	timeslotset.add(tstart)
	return '\t<h3 class="time-slot" style="grid-row: time-{0};">{1}</h3>\n\n'.format(to_css(tstart),tstart)

def make_full_track(talk, session, timeslotset, numtrk):
	start = talk["StartTime"]
	stop = talk["EndTime"]
	output = make_timeslot(timeslotset, start)
	output += '\t<div class="session session-{0} track-all" style="grid-column: track-1-start / track-{3}-end; grid-row: time-{1} / time-{2};">\n'.format(session,to_css(start),to_css(stop),numtrk)

	output += '\t\t<span class="session-time">{0} - {1}</span>\n'.format(start,stop)
	output += '\t\t<br>\n'

	output += '\t\t<h4 class="session-title">{0}</h4>\n'.format(talk["Title"])

	if not pd.isna(talk["Description"]):
		output += '\t\t<span class="session-description">{0}</span>\n'.format(talk["Description"])
	output += '\t</div>\n\n'
	return output

def make_track(talk,session,timeslotset,trkid=1,roomname=None):

	start = talk["StartTime"]
	stop = talk["EndTime"]
	authors = get_authors(talk)

	output = make_timeslot(timeslotset, start)

	output += '\t<div class="session session-{0} track-{3}" style="grid-column: track-{3}; grid-row: time-{1} / time-{2};">\n'.format(session,to_css(start),to_css(stop),trkid)

	toplefttext = roomname
	if toplefttext is not None and not pd.isna(trkname := talk['Track']):
		toplefttext += '<br>' + trkname

	output += '\t\t<span class="session-time">{0} - {1}</span>\n'.format(start,stop)
	if toplefttext is not None:
		output += '\t\t<span class="session-track">{0}</span>\n'.format(toplefttext)

	output += '\t\t<br>\n'
	output += '\t\t<h4 class="session-title">{0}</h4>\n'.format(talk["Title"])
	output += '\t\t<h4 class="session-presenter">{0}\n\t\t</h4>\n'.format(authors)

	needextrabr = False

	if not pd.isna(talk["Links"]):
		needextrabr = True
		link = talk["Links"].split("\n")[0]
		output += '\t\t<a href="{0}" target="_blank" style="color:white" class="video-link">🤖 Ver código</a><br>\n'.format(link)

	if not pd.isna(talk["Documentation"]):
		needextrabr = True
		link = talk["Documentation"].split("\n")[0]
		output += '\t\t<a href="{0}" target="_blank" style="color:white" class="video-link">🌐 Leer más</a><br>\n'.format(link)

	if not pd.isna(talk["Video"]):
		needextrabr = True
		link = talk["Video"].split("\n")[0]
		output += '\t\t<a href="{0}" target="_blank" style="color:white" class="video-link">🎞 Vídeo</a><br>\n'.format(link)

	if needextrabr:
		output += '\t\t<br>\n'

	if not pd.isna(talk["Description"]):
		descr = markdown(talk["Description"])
		numwords = len(re.findall(r'\w+', descr))
		verylong = numwords > 100
		if verylong:
			output += '\t\t<details class="session-description">\n'
			output += '\t\t<summary>Ver descripción</summary>\n'
		output += descr + '\n'
		if verylong:
			output += '\t\t</details>\n'

	output += '\t</div>\n\n'
	return output

def make_day(csv, day_string="", tracks=['Track 1', 'Track 2']):
	output = "## {0}\n\n".format(day_string)
	output += f'<div class="schedule_{len(tracks)}tracks" aria-labelledby="schedule-heading">\n'
	for i,trk in enumerate(tracks):
		output += f'\t<span class="track-slot" aria-hidden="true" style="grid-column: track-{i+1}; grid-row: tracks;">{trk}</span>\n'

	start_t = "StartTime"
	track = "TrackId"

	# In theory this should work
	day = csv.copy()
	day["start_int"] = day[start_t].tolist()
	day["start_int"] = day["start_int"].apply(lambda x: datetime.datetime.strptime(str(x), "%H:%M"))
	day = day.sort_values(by=["start_int",track])

	session = 1
	tset = set()
	for row in day.iterrows():
		talk = row[1]
		trkid = talk[track]
		if trkid == 0:
			output += make_full_track(talk, session, tset, len(tracks))
		else:
			output += make_track(talk, session, tset, trkid, tracks[trkid-1])
		session += 1

	output += '</div>\n'
	return output

if __name__ == "__main__":
	# Spreadsheet is at:
	# https://docs.google.com/spreadsheets/d/19QoWA-dk2TPwVKJ93Yj0Lw1zkAzOOc73-jZMkkOeV0k/edit?usp=sharing

	# To run, copy spreadsheet to schedule_csv
	# run: python3 MakeROSConSchedule.py > ../_posts/2000-01-06-program.md
	schedule_csv = "ROSConES2024Schedule.csv"

	schedule = pd.read_csv(schedule_csv)

	sd = "Date"
	days = schedule[sd].unique()

	# Break down the sessions by days
	day1 = schedule[schedule[sd]==days[0]]
	day2 = schedule[schedule[sd]==days[1]]

	# Print it all out
	output = ""
	output += make_day(day1, "Workshops/Tutoriales - 19 de septiembre de 2024", [ 'Ed. 45, Planta 1, Aula 05', 'Ed. 45, Planta 1, Aula 06', 'Ed. 45, Planta 1, Aula 07' ])
	output += make_day(day2, "Charlas Técnicas - 20 de septiembre de 2024", [ 'Paraninfo', 'Sala de Grados, Ed. 7' ])

	print(output)
