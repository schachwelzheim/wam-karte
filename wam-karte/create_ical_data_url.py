import urllib.parse
from config import URL

def create_ical_data_url(title, location, date_start_iso, date_ical_end_iso, description=""):
    """
    Erzeugt eine iCal-Data-URI für ganztägige (auch mehrtägige) Events.
    Für ganztägige Termine gilt nach RFC 5545:
    - Single Day (z.B. 25.10.): DTSTART=20261025, DTEND=20261026
    - Multi Day (z.B. 25.-26.10.): DTSTART=20261025, DTEND=20261027
    """
    dt_start = date_start_iso.replace("-", "").strip()
    
    # Falls kein abweichendes iCal-Enddatum übergeben wurde, ist DTEND = Startdatum + 1 Tag
    if date_ical_end_iso and date_ical_end_iso.strip():
        dt_end = date_ical_end_iso.replace("-", "").strip()
    else:
        # Fallback auf 1 Tag nach Start
        dt_end = dt_start

    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Schachverband Baden-Wuerttemberg//Turnierkarte//DE
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
SUMMARY:{title}
LOCATION:{location}
DESCRIPTION:{description}
DTSTART;VALUE=DATE:{dt_start}
DTEND;VALUE=DATE:{dt_end}
STATUS:CONFIRMED
TRANSP:TRANSPARENT
END:VEVENT
END:VCALENDAR"""

    encoded_ics = urllib.parse.quote(ics_content.strip())
    return f"data:text/calendar;charset=utf8,{encoded_ics}"
