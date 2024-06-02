package utils

func MultiString(char string, repeat int) string {
	final := ""
	for i := 0; i < repeat; i++ {
		final += char
	}
	return final
}
