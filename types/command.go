package types

var Commands []Command

type Command struct {
	Name string
	Args []Argument
	Help string
	Run  func(cmd *Command, args []string)
}

type Argument struct {
	Name     string
	Required bool
}
