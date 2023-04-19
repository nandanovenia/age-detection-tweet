import regex as re
import datetime
import math

currentDate = datetime.date.today()
year_now=currentDate.year
class agedetection_rule():
    
    def regex_age1(text):
        regex_digits=re.compile(r"\d{2}")
        match = re.search(r"\b(umur\s*|usia\s*|umurku\s*|usiaku\s*)\d{2}\s*", text,flags=re.I)
        if match:
            match_digits=regex_digits.findall(match.group())
            quantity=int(match_digits[0])
            return quantity
        
    def regex_age2(text):
        regex_digits=re.compile(r"\d+")
        match = re.search(r"\b\s*(f|m|co|ce|cowok|cewek|cwk|girl|boy|pria|perempuan|wanita)\s*?(-)?\d{1,2}\s*\b", text,flags=re.I)
        if match:
            match_digits=regex_digits.findall(match.group())
            quantity=int(match_digits[0])
            return quantity
        
    def regex_age3(text):
        regex_digits=re.compile(r"\d+")
        match = re.search(r"\b\s*\d{1,2}\s*(th|tahun|thn|yo)\s*\b", text,flags=re.I)
        if match:
            match_digits=regex_digits.findall(match.group())
            quantity=int(match_digits[0])
            return quantity

    def regex_year1(text):
        regex_digits=re.compile(r"\d+")
        match = re.search(r"\b(born\s*)(in\s*|at\s*|on\s*)\d{4}\s*", text,flags=re.I)
        if match:
            match_digits=regex_digits.findall(match.group())
            quantity=int(match_digits[0])
            age=year_now-quantity
            return age
        
    def regex_year2(text):
        regex_digits=re.compile(r"\d+")
        match = re.search(r"\b(lahir\s*|kelahiran\s*)(di\s*)?\d{4}\s*", text,flags=re.I)
        if match:
            match_digits=regex_digits.findall(match.group())
            quantity=int(match_digits[0])
            age=year_now-quantity
            return age

    def regex_year3(text):
        try:
            valid_year = re.compile(r'\b(19[89][0-9]|200[0-9]|201[0-5])\b')
            year=int(valid_year.search(text).group())
            age=year_now-year
            return age
        except:
            pass