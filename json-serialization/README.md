### Results

Source app: 

```MainWindow[Layout[LineEdit: 20, LineEdit: 30], Layout[ComboBox: [1, 2, 3, 4], ComboBox: ['a', 'b', 'c']]]```

Serialized to JSON data:

```
{
  "MainWindow": {
    "title": "Application"
  },
  "children": [
    {
      "Layout": {
        "alignment": 1
      },
      "children": [
        {
          "LineEdit": {
            "max_length": 20
          },
          "children": []
        },
        {
          "LineEdit": {
            "max_length": 30
          },
          "children": []
        }
      ]
    },
    {
      "Layout": {
        "alignment": 2
      },
      "children": [
        {
          "ComboBox": {
            "items": [
              1,
              2,
              3,
              4
            ]
          },
          "children": []
        },
        {
          "ComboBox": {
            "items": [
              "a",
              "b",
              "c"
            ]
          },
          "children": []
        }
      ]
    }
  ]
}
```

Parsed from JSON: 

```MainWindow[Layout[LineEdit: 20, LineEdit: 30], Layout[ComboBox: [1, 2, 3, 4], ComboBox: ['a', 'b', 'c']]]```
