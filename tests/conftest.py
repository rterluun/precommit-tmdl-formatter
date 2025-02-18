# flake8: noqa
import pytest

MEASURES_SORTED_IN_STRING = """
table _measures
    lineageTag: 06e2dbdd-c3ac-405b-8a81-5aa4912861b3

    measure 'Measure a' = [field1]-[field2]
        formatString: #,0
        displayFolder: Folder1\Folder2
        lineageTag: 65e1c794-4323-4801-b808-a320bf7f5abb

        annotation PBI_FormatHint = {"isGeneralNumber":false}

    measure 'Measure b' = SUM('field1'[Count])
        formatString: #,0
        displayFolder: Folder1\Folder2
        lineageTag: 357ac151-baaf-47c6-92ff-033eeacdeb60

        annotation PBI_FormatHint = {"isGeneralNumber":true}

    measure 'Measure c' = [field1]-[field2]
        formatString: #,0
        displayFolder: Folder1\Folder2
        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb

    measure Measure d = [field1]-[field2]
        formatString: #,0
        displayFolder: Folder1\Folder2
        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb

    measure 'Measure e' = [field1]-[field2]
        formatString: #,0
        displayFolder: Folder1\Folder2
        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb
    """

CAPITALIZED_COLUMN_NAMES = """
table 'my_table'
	lineageTag: e4a415f7-c1f5-45cb-928b-1070ad5686ae

	column 'Street name'
		dataType: string
		lineageTag: 839a64af-d1f7-4d47-a01a-d27cd156ef01
		sourceColumn: street_name

	column 'City name'
		dataType: string
		lineageTag: 839a64af-d1f7-4d48-a01a-d27cd156ef01
		sourceColumn: city_name

	column 'Area name'
		dataType: string
		lineageTag: 839a64af-d1f7-4d49-a01a-d27cd156ef01
		sourceColumn: area_name
    """


@pytest.fixture
def measures_in_string():
    return """
table _measures
    lineageTag: 06e2dbdd-c3ac-405b-8a81-5aa4912861b3

    measure 'Measure a' = [field1]-[field2]
        formatString: #,0
        displayFolder: Folder1\\Folder2
        lineageTag: 65e1c794-4323-4801-b808-a320bf7f5abb

        annotation PBI_FormatHint = {"isGeneralNumber":false}

    measure 'Measure c' = [field1]-[field2]
        formatString: #,0
        displayFolder: Folder1\\Folder2
        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb

    measure 'Measure b' = SUM('field1'[Count])
        formatString: #,0
        displayFolder: Folder1\\Folder2
        lineageTag: 357ac151-baaf-47c6-92ff-033eeacdeb60

        annotation PBI_FormatHint = {"isGeneralNumber":true}

    measure 'Measure e' = [field1]-[field2]
        formatString: #,0
        displayFolder: Folder1\\Folder2
        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb

    measure Measure d = [field1]-[field2]
        formatString: #,0
        displayFolder: Folder1\\Folder2
        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb
    """


@pytest.fixture
def unsorted_measures_in_list():
    return [
        "\n\n    measure 'Measure a' = [field1]-[field2]\n        formatString: #,0\n        displayFolder: Folder1\\Folder2\n        lineageTag: 65e1c794-4323-4801-b808-a320bf7f5abb\n\n        annotation PBI_FormatHint = {\"isGeneralNumber\":false}\n",
        "\n    measure 'Measure c' = [field1]-[field2]\n        formatString: #,0\n        displayFolder: Folder1\\Folder2\n        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb\n",
        "\n    measure 'Measure b' = SUM('field1'[Count])\n        formatString: #,0\n        displayFolder: Folder1\\Folder2\n        lineageTag: 357ac151-baaf-47c6-92ff-033eeacdeb60\n\n        annotation PBI_FormatHint = {\"isGeneralNumber\":true}\n",
        "\n    measure 'Measure e' = [field1]-[field2]\n        formatString: #,0\n        displayFolder: Folder1\\Folder2\n        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb\n",
        "\n    measure Measure d = [field1]-[field2]\n        formatString: #,0\n        displayFolder: Folder1\\Folder2\n        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb\n",
    ]


@pytest.fixture
def sorted_measures_in_list():
    return [
        "\n\n    measure 'Measure a' = [field1]-[field2]\n        formatString: #,0\n        displayFolder: Folder1\\Folder2\n        lineageTag: 65e1c794-4323-4801-b808-a320bf7f5abb\n\n        annotation PBI_FormatHint = {\"isGeneralNumber\":false}\n",
        "\n    measure 'Measure b' = SUM('field1'[Count])\n        formatString: #,0\n        displayFolder: Folder1\\Folder2\n        lineageTag: 357ac151-baaf-47c6-92ff-033eeacdeb60\n\n        annotation PBI_FormatHint = {\"isGeneralNumber\":true}\n",
        "\n    measure 'Measure c' = [field1]-[field2]\n        formatString: #,0\n        displayFolder: Folder1\\Folder2\n        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb\n",
        "\n    measure Measure d = [field1]-[field2]\n        formatString: #,0\n        displayFolder: Folder1\\Folder2\n        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb\n",
        "\n    measure 'Measure e' = [field1]-[field2]\n        formatString: #,0\n        displayFolder: Folder1\\Folder2\n        lineageTag: 65e1c794-4323-4801-b404-a320bf7f5abb\n",
    ]


@pytest.fixture
def columns_in_string():
    return """
table 'my_table'
	lineageTag: e4a415f7-c1f5-45cb-928b-1070ad5686ae

	column street name
		dataType: string
		lineageTag: 839a64af-d1f7-4d47-a01a-d27cd156ef01
		sourceColumn: street_name

	column 'city name'
		dataType: string
		lineageTag: 839a64af-d1f7-4d48-a01a-d27cd156ef01
		sourceColumn: city_name

	column AREA name
		dataType: string
		lineageTag: 839a64af-d1f7-4d49-a01a-d27cd156ef01
		sourceColumn: area_name
    """
