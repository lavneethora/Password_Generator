# Password Generator

## Overview

This Python program is a **Password Generator** that creates random, strong passwords based on user-specified criteria. It is designed to help users generate secure passwords that can include letters (uppercase and lowercase), numbers, and special characters. The length of the password is customizable, ensuring that the generated passwords meet the user’s security needs.

## Key Features

- **Customizable Length**: Users can specify the desired length of the password.
- **Character Options**: Users can choose to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (e.g., `!@#$%^&*()`)
- **Randomized Passwords**: The program uses Python's `random` and `string` modules to generate unpredictable and secure passwords.
- **User-Friendly**: Simple input prompts guide the user through password creation.

## How to Use the Program

1. **Run the Program**: Execute the Python script in a terminal or console.
2. **Enter Password Length**: Input the desired length of the password.
3. **Choose Character Sets**: Select whether to include uppercase letters, lowercase letters, numbers, and special characters.
4. **Generate Password**: The program outputs a randomly generated password based on the selected options.

## Sample Usage

```bash
Enter the desired password length: 12
Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): yes

Generated Password: fS3&kL7!xWzQ
```

## Program Structure

- **Main Function**: Manages the user input and character selection process.
- **Password Generation**: Based on the user's choices, the program assembles a pool of characters and randomly selects from it to generate the password.
- **Randomization**: The random module is used to ensure unpredictable password generation.

## Password Character Sets:

- Uppercase Letters: A-Z
- Lowercase Letters: a-z
- Numbers: 0-9
- Special Characters: !@#$%^&*()_+-=[]{}|;:'",.<>?/

## Example of Running the Program

##Run the Program
```bash
python password_generator.py
```

## Example Output
```bash
Enter the desired password length: 16
Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): no

Generated Password: A4tXgWqzDf5Hm6Rj
```

## Future Improvements

- **Password Strength Indicator**: Implement a feature to rate the strength of the generated password based on common security criteria.
- **Copy to Clipboard**: Add functionality to copy the generated password to the system clipboard for easy use.
- **GUI Version**: Implement a graphical interface using Tkinter for more user-friendly interaction.

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
- Feel free to submit issues or pull requests for any improvements or bug fixes.

## Author

- Lavneet Hora
- Sophomore @ Texas Tech University
- Computer Science
