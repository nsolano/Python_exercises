import pytest
from rick_riddle import solution, has_no_double_letters

class TestSolution:

    def test_input_validation(self):
        long_riddle = "?" * 100001    

        with pytest.raises(ValueError):
            solution("ab?1c?") # Invalid character
            solution("ab?AC?") # Uppercase letters
            solution("aba?c")  # Duplicated letter
            solution(long_riddle) # Long riddle

    def test_functionality(self):
        assert "abcaca" in solution("ab?ac?")        
        assert "tests" in solution("?????")
        assert "a" in solution("?") # Single question mark
        assert len(solution("a??")) == 625  # 625 solutions
        with pytest.raises(ValueError):
            solution("aa?aa")  # No valid solution
