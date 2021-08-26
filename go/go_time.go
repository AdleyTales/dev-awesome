func main() {
	t := time.Now()

	fmt.Println(t.Year())
	fmt.Println(int(t.Month()))
	fmt.Println(t.Day())

	fmt.Println(strings.Repeat("*", 80))

	y,m,d := t.Date()
	fmt.Println(y)
	fmt.Println(m)
	fmt.Println(d)

	fmt.Println(strings.Repeat("*", 80))

	fmt.Println(t.Hour())
	fmt.Println(t.Minute())
	fmt.Println(t.Second())

	fmt.Println(t.Unix())
	fmt.Println(t.UnixNano())

	s := t.Format("2006-01-02 15:04:05")
	fmt.Println(s)

	s1 := t.Format("2006/01/02 15:04:05")
	fmt.Println(s1)

	ss := "2018-12-22 15:03:02"
	t,_ = time.Parse("2006-01-02 15:04:05", ss)
	fmt.Println(t)
}