from typing import Optional, List
from pathlib import Path
from dataclasses import dataclass
from tokenize import tokenize

import info_strings


@dataclass
class BannedToken:
    """A small structure to hold the position of a banned token. Used for highlighting"""

    line: int
    pos: int
    length: int


@dataclass
class BannedTokensValidationError:
    """Represents an error when the student used banned tokens. All occurrences of all tokens are counted"""

    violations: List[BannedToken]


@dataclass
class RequiredTokensValidationError:
    """Represents an error when the student did not use required tokens"""

    missing_tokens: List[str]


@dataclass
class ValidationResult:
    """Represents results of validation. If error is None, then there was no violation"""

    submission: Path
    banned_tokens_error: Optional[BannedTokensValidationError]
    required_tokens_error: Optional[RequiredTokensValidationError]

    def has_errors(self):
        return (
            self.banned_tokens_error is not None
            or self.required_tokens_error is not None
        )


class Validator:
    """Validates submissions by checking the presence of banned and required code tokens"""

    @staticmethod
    def _validate_banned_tokens(
        file_path: Path,
        banned_tokens: List[str],
    ) -> Optional[BannedTokensValidationError]:
        """Checks the submission and returns an Error with all violations if any. If none, returns None"""
        ans = []
        with open(file_path, "rb") as file_handler:
            for token in tokenize(file_handler.readline):
                if token.string in banned_tokens:
                    banned_token = BannedToken(
                        line=token.start[0],
                        pos=token.start[1],
                        length=len(token.string),
                    )
                    ans.append(banned_token)

        if ans:
            return BannedTokensValidationError(ans)
        return None

    @staticmethod
    def _validate_required_tokens(
        file_path: Path,
        required_tokens: List[str],
    ) -> Optional[RequiredTokensValidationError]:
        """Checks the submission and returns an Error if at least one of the required tokens is not present"""
        occurrences = {token: 0 for token in required_tokens}

        # count the number of occurrences of each required token
        with open(file_path, "rb") as file_handler:
            for token in tokenize(file_handler.readline):
                if token.string in required_tokens:
                    occurrences[token.string] += 1

        # find tokens with 0 occurrences
        ans = []
        for key in required_tokens:
            if occurrences[key] == 0:
                ans.append(key)

        if ans:
            return RequiredTokensValidationError(ans)
        return None

    @staticmethod
    def validate(
        file_path: Path,
        required_tokens: List[str],
        banned_tokens: List[str],
    ) -> Optional[ValidationResult]:
        """
        Validates the given submission by checking the presence of banned and required code tokens.
        Returns `None` if no errors were found, `ValidationResult` otherwise.
        """

        assert file_path.exists(), info_strings.ERR_SUBMISSION_DOES_NOT_EXIST

        result = ValidationResult(
            file_path,
            Validator._validate_banned_tokens(file_path, banned_tokens),
            Validator._validate_required_tokens(file_path, required_tokens),
        )

        if result.has_errors():
            return result
        return None
