package trace

import (
	"runtime"
	"strings"
)

type Trace struct {
	Error      error
	FileName   string
	Line       int
	FuncName   string
	Package    string
	SubPackage string
}

func GenerateTrace(err error, pc uintptr, filename string, line int) Trace {
	fullFuncName := runtime.FuncForPC(pc).Name()
	funcNameParts := strings.Split(fullFuncName, "/")
	subPackage := strings.Split(funcNameParts[len(funcNameParts)-1], ".")[0]
	funcName := strings.Split(funcNameParts[len(funcNameParts)-1], ".")[1]
	funcPackage := strings.Trim(fullFuncName, "/"+subPackage+"."+funcName)

	return Trace{
		Error:      err,
		FileName:   filename,
		Line:       line,
		FuncName:   funcName,
		Package:    funcPackage,
		SubPackage: subPackage,
	}
}
