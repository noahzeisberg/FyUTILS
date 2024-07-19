package typing

type Command struct {
	Name  string
	Short string
	Args  []Argument
	Run   func([]string)
}

type Argument struct {
	Identifier string
	Required   bool
}

type T struct {
}

func (cmd Command) Register(list *[]Command) {
	*list = append(*list, cmd)
}

type PathAlias struct {
	Short string
	Path  string
}
