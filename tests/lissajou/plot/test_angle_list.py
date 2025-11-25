"""Tests for the angle_list function."""

import math

import pytest

from lissajou.plot import angle_list


class TestAngleListValid:
    """Tests for valid angle_list inputs."""

    def test_angle_list_with_delta_1(self) -> None:
        """Test angle_list with delta=1 returns sequential angles."""
        result: list[int] = angle_list(1)
        assert len(result) == 360
        assert result == list(range(360))

    def test_angle_list_with_delta_7(self) -> None:
        """Test angle_list with delta=7 (coprime with 360)."""
        result: list[int] = angle_list(7)
        # gcd(7, 360) = 1, so n = 360
        assert len(result) == 360
        assert sorted(result) == list(range(360))
        # Verify the formula
        expected: list[int] = [(7 * i) % 360 for i in range(360)]
        assert result == expected

    def test_angle_list_with_delta_2(self) -> None:
        """Test angle_list with delta=2 (even, shares factor with 360)."""
        result: list[int] = angle_list(2)
        # gcd(2, 360) = 2, so n = 180
        assert len(result) == 180
        # Should be all even angles
        expected: list[int] = [(2 * i) % 360 for i in range(180)]
        assert result == expected
        assert all(angle % 2 == 0 for angle in result)

    def test_angle_list_with_delta_10(self) -> None:
        """Test angle_list with delta=10."""
        result: list[int] = angle_list(10)
        # gcd(10, 360) = 10, so n = 36
        assert len(result) == 36
        # Should be all multiples of 10
        expected: list[int] = [(10 * i) % 360 for i in range(36)]
        assert result == expected

    def test_angle_list_with_delta_180(self) -> None:
        """Test angle_list with delta=180."""
        result: list[int] = angle_list(180)
        # gcd(180, 360) = 180, so n = 2
        assert len(result) == 2
        expected: list[int] = [0, 180]
        assert result == expected

    def test_angle_list_with_delta_359(self) -> None:
        """Test angle_list with delta=359 (coprime with 360)."""
        result: list[int] = angle_list(359)
        # gcd(359, 360) = 1, so n = 360
        assert len(result) == 360
        assert sorted(result) == list(range(360))

    def test_angle_list_length_formula(self) -> None:
        """Test that length is always 360 / gcd(delta, 360)."""
        for delta in [1, 7, 11, 13, 17, 97]:  # Coprime with 360
            result: list[int] = angle_list(delta)
            m: int = math.gcd(delta, 360)
            n: int = 360 // m
            assert len(result) == n

    def test_angle_list_formula(self) -> None:
        """Test that angles follow the formula (delta * i) % 360."""
        delta: int = 17
        result: list[int] = angle_list(delta)
        m: int = math.gcd(delta, 360)
        n: int = 360 // m
        for i in range(n):
            expected_angle: int = (delta * i) % 360
            assert result[i] == expected_angle


class TestAngleListInvalid:
    """Tests for invalid angle_list inputs."""

    def test_angle_list_with_zero(self) -> None:
        """Test angle_list raises ValueError for delta=0."""
        with pytest.raises(ValueError, match="delta must be positive"):
            angle_list(0)

    def test_angle_list_with_negative(self) -> None:
        """Test angle_list raises ValueError for negative delta."""
        with pytest.raises(ValueError, match="delta must be positive"):
            angle_list(-5)

    def test_angle_list_with_360(self) -> None:
        """Test angle_list raises ValueError for delta=360."""
        with pytest.raises(ValueError, match="delta must be less than 360"):
            angle_list(360)

    def test_angle_list_with_greater_than_360(self) -> None:
        """Test angle_list raises ValueError for delta > 360."""
        with pytest.raises(ValueError, match="delta must be less than 360"):
            angle_list(500)


class TestAngleListExamples:
    """Test specific examples of angle_list behavior."""

    def test_angle_list_delta_3(self) -> None:
        """Test angle_list with delta=3."""
        result: list[int] = angle_list(3)
        # gcd(3, 360) = 3, so n = 120
        assert len(result) == 120
        # All angles should be multiples of 3
        assert all(angle % 3 == 0 for angle in result)
        # Verify formula
        expected: list[int] = [(3 * i) % 360 for i in range(120)]
        assert result == expected

    def test_angle_list_delta_5(self) -> None:
        """Test angle_list with delta=5."""
        result: list[int] = angle_list(5)
        # gcd(5, 360) = 5, so n = 72
        assert len(result) == 72
        # All angles should be multiples of 5
        assert all(angle % 5 == 0 for angle in result)

    def test_angle_list_delta_90(self) -> None:
        """Test angle_list with delta=90."""
        result: list[int] = angle_list(90)
        # gcd(90, 360) = 90, so n = 4
        assert len(result) == 4
        expected: list[int] = [0, 90, 180, 270]
        assert result == expected

    def test_angle_list_delta_120(self) -> None:
        """Test angle_list with delta=120."""
        result: list[int] = angle_list(120)
        # gcd(120, 360) = 120, so n = 3
        assert len(result) == 3
        expected: list[int] = [0, 120, 240]
        assert result == expected
