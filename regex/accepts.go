package regex

import "regexp"

var (
	AcceptsIP   = regexp.MustCompile("^(1-255).(1-255).(1-255).(1-255)$")
	AcceptsPort = regexp.MustCompile("^(1-65536)$")
	AcceptsAny  = regexp.MustCompile("^*$")
)
