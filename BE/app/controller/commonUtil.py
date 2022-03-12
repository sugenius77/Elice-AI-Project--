class Region():

    region_code = {
        '000': ['서울', '부산', '제주', '강원', '여수'],
        '002': '서울',
        '033': '강원',
        '051': '부산',
        '061': '여수',
        '064': '제주'
    }

    def transRegion(self, region):
        try:
            region_list = region.split("|")
            if len(region_list) >= 1 and '000' in region_list:
                result = self.region_code['000']
            else:

                result = list(map(lambda x: self.region_code[x], region_list))
            return result
        except:
            return 400
