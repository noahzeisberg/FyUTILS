package main

import "regexp"

type Group struct {
	A any
	B any
}

type Command struct {
	Name  string
	Short string
	Args  []Argument
	Run   func([]string)
}

type Argument struct {
	Identifier string
	Required   bool
	Expect     *regexp.Regexp
}

type AddressInformation struct {
	IP            string                `json:"ip"`
	Type          string                `json:"type"`
	Continent     string                `json:"continent"`
	ContinentCode string                `json:"continent_code"`
	Country       string                `json:"country"`
	CountryCode   string                `json:"country_code"`
	Region        string                `json:"region"`
	RegionCode    string                `json:"region_code"`
	City          string                `json:"city"`
	Latitude      float64               `json:"latitude"`
	Longitude     float64               `json:"longitude"`
	IsEU          bool                  `json:"is_eu"`
	PostalCode    string                `json:"postal"`
	CallingCode   string                `json:"calling_code"`
	Capital       string                `json:"capital"`
	Connection    ConnectionInformation `json:"connection"`
	Timezone      TimezoneInformation   `json:"timezone"`
}

type ConnectionInformation struct {
	SystemNumber    int    `json:"asn"`
	Organisation    string `json:"org"`
	ServiceProvider string `json:"isp"`
	ISPDomain       string `json:"domain"`
}

type TimezoneInformation struct {
	ID           string `json:"id"`
	Abbreviation string `json:"abbr"`
	UTC          string `json:"utc"`
}

type PathAlias struct {
	Short string
	Path  string
}

type FuelPackage struct {
	Owner      string `json:"owner"`
	Repository string `json:"repository"`
	Branch     string `json:"branch"`
}
