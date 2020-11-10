class TestFactory:
    type_map = {
        'EINS' : 1,
        'ZWEI' : 2
    }
    
    @staticmethod
    def get_result(key) -> int:
        result = TestFactory.type_map.get(key)
        return result

if __name__ == '__main__':
    print(TestFactory.get_result('EINS'))