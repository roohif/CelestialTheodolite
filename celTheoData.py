import math

EARTH_RADIUS = 6371008.8 # This is the radius that the python haversine library uses
METRES_PER_DEGREE = EARTH_RADIUS * 2 * math.pi / 360

HEFFRON_ELEVATION = 2075 # m
HEFFRON_PRESSURE = 788 # hPa

observer = { "lat": REDACTED, "lon": REDACTED, "elevation": HEFFRON_ELEVATION }

peaks = {
	"Blodgett Peak": { "name": "Blodgett Peak", "lat": 38.958889, "lon":-104.907222, "elevation": 2870.0, "distance": 35910, "deltaHeight": 794.92 },
	"Blue Mountain": { "name": "Blue Mountain", "lat": 38.693889, "lon":-104.915833, "elevation": 3000.8, "distance": 49770, "deltaHeight": 925.72 },
	"Cheyenne Mountain": { "name": "Cheyenne Mountain", "lat": 38.743889, "lon":-104.862778, "elevation": 2883.1, "distance": 42630, "deltaHeight": 808.02 },
	"Green Mountain": { "name": "Green Mountain", "lat": 38.696111, "lon":-104.963333, "elevation": 3084.9, "distance": 52690, "deltaHeight": 1009.82 },
	"Greenhorn Mountain": { "name": "Greenhorn Mountain", "lat": 37.881389, "lon":-105.013333, "elevation": 3765.0, "distance": 132200, "deltaHeight": 1692.82 },
	"Mount Rosa": { "name": "Mount Rosa", "lat": 38.754166, "lon":-104.948059, "elevation": 3506.0, "distance": 47730, "deltaHeight": 1430.92 },
	"Pikes Peak": { "name": "Pikes Peak", "lat": 38.840278, "lon":-105.044444, "elevation": 4299.8, "distance": 50700, "deltaHeight": 2226.12 }
}

blyn = {
	"Blyn Mountain": { "name": "Blyn Mountain", "lat": 48.017222, "lon":-122.926111, "elevation": 646, "distance": 40962, "deltaHeight": 640 }
}

observations = [
	{ "timestamp": "2025-01-28T01:43:07", "peak": "Pikes Peak", "star": "39 Aqr", "recordedAngle": 2.567500, "celTheoAngle": 2.556870, "apparentAngle": 2.320012 },
	{ "timestamp": "2025-01-28T02:31:40", "peak": "Pikes Peak", "star": "HD 217533", "recordedAngle": 2.573111, "celTheoAngle": 2.563325, "apparentAngle": 2.326145 },
	{ "timestamp": "2025-01-31T01:31:22", "peak": "Pikes Peak", "star": "39 Aqr", "recordedAngle": 2.557028, "celTheoAngle": 2.548565, "apparentAngle": 2.312122 },
	{ "timestamp": "2025-01-31T01:36:02", "peak": "Pikes Peak", "star": "HD 211410", "recordedAngle": 2.567944, "celTheoAngle": 2.557789, "apparentAngle": 2.320885 },
	{ "timestamp": "2025-01-31T02:19:19", "peak": "Pikes Peak", "star": "HD 217429", "recordedAngle": 2.572694, "celTheoAngle": 2.562565, "apparentAngle": 2.325423 },
	{ "timestamp": "2025-01-31T02:21:19", "peak": "Pikes Peak", "star": "HD 217721", "recordedAngle": 2.561639, "celTheoAngle": 2.551642, "apparentAngle": 2.315044 },
	{ "timestamp": "2025-01-31T02:52:44", "peak": "Pikes Peak", "star": "HD 221665", "recordedAngle": 2.554583, "celTheoAngle": 2.544648, "apparentAngle": 2.308401 },
	{ "timestamp": "2025-01-31T02:58:27", "peak": "Pikes Peak", "star": "102 Aqr", "recordedAngle": 2.548333, "celTheoAngle": 2.537778, "apparentAngle": 2.301876 },
	{ "timestamp": "2025-01-31T03:08:28", "peak": "Pikes Peak", "star": "HD 223559", "recordedAngle": 2.561694, "celTheoAngle": 2.551433, "apparentAngle": 2.314846 },
	{ "timestamp": "2025-01-31T03:10:51", "peak": "Pikes Peak", "star": "HD 223774", "recordedAngle": 2.578806, "celTheoAngle": 2.568591, "apparentAngle": 2.331149 },
	{ "timestamp": "2025-01-31T03:45:31", "peak": "Pikes Peak", "star": "HD 2345", "recordedAngle": 2.566250, "celTheoAngle": 2.555679, "apparentAngle": 2.318880 },
	{ "timestamp": "2025-02-01T01:27:25", "peak": "Pikes Peak", "star": "39 Aqr", "recordedAngle": 2.563222, "celTheoAngle": 2.551860, "apparentAngle": 2.315252 },
	{ "timestamp": "2025-02-01T02:13:47", "peak": "Pikes Peak", "star": "TYC 5826-746-1", "recordedAngle": 2.553944, "celTheoAngle": 2.536997, "apparentAngle": 2.301133 },
	{ "timestamp": "2025-02-01T02:15:57", "peak": "Pikes Peak", "star": "HD 217533", "recordedAngle": 2.571806, "celTheoAngle": 2.561352, "apparentAngle": 2.324270 },
	{ "timestamp": "2025-02-01T02:54:23", "peak": "Pikes Peak", "star": "102 Aqr", "recordedAngle": 2.571556, "celTheoAngle": 2.562432, "apparentAngle": 2.325296 },
	{ "timestamp": "2025-02-01T03:04:33", "peak": "Pikes Peak", "star": "HD 223559", "recordedAngle": 2.558306, "celTheoAngle": 2.548639, "apparentAngle": 2.312192 },
	{ "timestamp": "2025-02-01T03:06:57", "peak": "Pikes Peak", "star": "HD 223774", "recordedAngle": 2.572278, "celTheoAngle": 2.562744, "apparentAngle": 2.325593 },
	{ "timestamp": "2025-02-08T02:06:56", "peak": "Blodgett Peak", "star": "LP Aqr", "recordedAngle": 1.202028, "celTheoAngle": 1.192484, "apparentAngle": 1.167991 },
	{ "timestamp": "2025-02-08T02:20:24", "peak": "Blodgett Peak", "star": "HD 216718", "recordedAngle": 1.196250, "celTheoAngle": 1.184588, "apparentAngle": 1.160743 },
	{ "timestamp": "2025-02-08T03:52:00", "peak": "Blodgett Peak", "star": "HD 2324", "recordedAngle": 1.198167, "celTheoAngle": 1.186061, "apparentAngle": 1.162095 },
	{ "timestamp": "2025-02-08T04:15:52", "peak": "Blodgett Peak", "star": "HD 4915", "recordedAngle": 1.205278, "celTheoAngle": 1.192971, "apparentAngle": 1.168438 },
	{ "timestamp": "2025-02-08T04:28:20", "peak": "Blodgett Peak", "star": "25 Cet", "recordedAngle": 1.204833, "celTheoAngle": 1.194645, "apparentAngle": 1.169977 },
	{ "timestamp": "2025-02-08T04:39:00", "peak": "Blodgett Peak", "star": "HD 7449", "recordedAngle": 1.214472, "celTheoAngle": 1.204059, "apparentAngle": 1.178619 },
	{ "timestamp": "2025-03-10T02:01:14", "peak": "Cheyenne Mountain", "star": "HD 13709", "recordedAngle": 1.013917, "celTheoAngle": 1.001089, "apparentAngle": 0.937803 },
	{ "timestamp": "2025-03-10T02:28:42", "peak": "Cheyenne Mountain", "star": "HD 16733", "recordedAngle": 1.018750, "celTheoAngle": 0.996127, "apparentAngle": 0.933294 },
	{ "timestamp": "2025-03-10T02:39:43", "peak": "Cheyenne Mountain", "star": "HD 17926", "recordedAngle": 1.004667, "celTheoAngle": 0.982116, "apparentAngle": 0.920564 },
	{ "timestamp": "2025-03-10T03:22:11", "peak": "Cheyenne Mountain", "star": "HD 22248", "recordedAngle": 1.032722, "celTheoAngle": 1.010044, "apparentAngle": 0.945945 },
	{ "timestamp": "2025-03-10T03:38:29", "peak": "Cheyenne Mountain", "star": "HD 24267", "recordedAngle": 1.026500, "celTheoAngle": 1.003791, "apparentAngle": 0.940259 },
	{ "timestamp": "2025-03-10T03:49:34", "peak": "Cheyenne Mountain", "star": "HD 25371", "recordedAngle": 1.021639, "celTheoAngle": 0.998864, "apparentAngle": 0.935784 },
	{ "timestamp": "2025-03-11T02:51:26", "peak": "Mount Rosa", "star": "HD 17320", "recordedAngle": 1.720667, "celTheoAngle": 1.711286, "apparentAngle": 1.549281 },
	{ "timestamp": "2025-03-11T03:00:52", "peak": "Mount Rosa", "star": "HD 18290", "recordedAngle": 1.722056, "celTheoAngle": 1.712680, "apparentAngle": 1.550579 },
	{ "timestamp": "2025-03-13T04:32:54", "peak": "Blue Mountain", "star": "HD 32515", "recordedAngle": 1.013028, "celTheoAngle": 1.005012, "apparentAngle": 0.882999 },
	{ "timestamp": "2025-03-13T04:34:43", "peak": "Blue Mountain", "star": "HD 32489", "recordedAngle": 1.032389, "celTheoAngle": 1.024392, "apparentAngle": 0.900574 },
	{ "timestamp": "2025-03-13T05:28:21", "peak": "Blue Mountain", "star": "HD 40248", "recordedAngle": 1.045778, "celTheoAngle": 1.037805, "apparentAngle": 0.912746 },
	{ "timestamp": "2025-03-15T04:02:58", "peak": "Green Mountain", "star": "HD 28388", "recordedAngle": 1.116667, "celTheoAngle": 1.080849, "apparentAngle": 0.927942 },
	{ "timestamp": "2025-03-15T05:29:28", "peak": "Green Mountain", "star": "HD 39891", "recordedAngle": 1.094222, "celTheoAngle": 1.083467, "apparentAngle": 0.930321 },
	{ "timestamp": "2025-03-15T05:33:45", "peak": "Green Mountain", "star": "HD 40555", "recordedAngle": 1.077222, "celTheoAngle": 1.064641, "apparentAngle": 0.913221 },
	{ "timestamp": "2025-03-17T02:40:25", "peak": "Greenhorn Mountain", "star": "HD 35182", "recordedAngle": 0.599694, "celTheoAngle": 0.595723, "apparentAngle": -0.134803 },
	{ "timestamp": "2025-03-17T02:50:02", "peak": "Greenhorn Mountain", "star": "HD 36889", "recordedAngle": 0.776889, "celTheoAngle": 0.772980, "apparentAngle": 0.018985 }
]
