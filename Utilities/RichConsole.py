# coding: utf-8

"""
    Rich Console
    Inspired by http://www.jchr.be/python/ecma-48.htm
    Allows basic formatting of console text (via print) based on ECMA-48 standard
    
    You can :
        - print a text with foreground and background color tags at a specific line/column position
        - clears the screen
        - show and hide cursor
    
        Possible enhancements :
        - move cursor up, down, left or right n times
        - insert or remove n lines at cursor position
        - define scroll area from line start to line end
        - save and recall cursor position
"""

# import modules
import os
import sys
import time
from enum import Enum

# protected variables, constants and enums
# _RichConsoleEnabled = False

class Format(Enum):
    Prefix = "\033["
    ForegroundPrefix = "3"
    BackgroundPrefix = "4"
    Reset = "0m"
    StyleAndColorSuffix = "m"
    PositionSuffix = "H"
    MoveUpSuffix = "A"
    MoveDownSuffix = "B"
    MoveRightSuffix = "C"
    MoveLeftSuffix = "D"
    ClearScreen = "2J"
    CursorVisible = "?25h"
    CursorInvisible = "?25l"

class Style(Enum):
    Bold = {"Tag" : "SB", "Format" : "1"}         # note that this is very subtle to see...
    Underline = {"Tag" : "SU", "Format" : "4"}
    Inverse = {"Tag" : "SI", "Format" : "7"}

class Color(Enum):
    Black = {"Tag" : "B", "Format" : "0"}
    Red = {"Tag" : "R", "Format" : "1"}
    Green = {"Tag" : "G", "Format" : "2"}
    Yellow = {"Tag" : "Y", "Format" : "3"}
    Blue = {"Tag" : "U", "Format" : "4"}
    Magenta = {"Tag" : "M", "Format" : "5"}
    Cyan = {"Tag" : "C", "Format" : "6"}
    White = {"Tag" : "W", "Format" : "7"}

class Justify(Enum):
    No = 0
    Left = 1
    Center = 2
    Right = 3

class PrintSpeed(Enum):     # in ms
    Instant = 0
    UltraFast = .01
    VeryFast = .02
    Fast = .04
    Medium = .08
    Slow = .15
    VerySlow = .3


# functions
def ClearConsole(
    Line = None, 
    Column = None,
    Width = None,
    Height = None,
    Character = " ",
    ForeColor = Color.White,
    BackColor = Color.Black):
    """
        Clear the console 
            - depending on OS (for full console)
            - or in a specified square with specified character and colors
    """

    if Line is None or Column is None or Width is None or Height is None:
        
        # full Console
        if "win" in sys.platform.lower():
            # for windows
            os.system("cls")
        elif "linux" in sys.platform.lower():
            # for linux
            os.system("clear")

    else:

        # specified square
        for CurrentLine in range(Height):
            BlankLine = (
                f"{Format.Prefix.value}{Format.ForegroundPrefix.value}{ForeColor.value['Format']};{Format.BackgroundPrefix.value}{BackColor.value['Format']}{Format.StyleAndColorSuffix.value}"
                + "".ljust(Width, Character)
                + f"{Format.Prefix.value}{Format.Reset.value}")
            print(
                f"{Format.Prefix.value}{Line + CurrentLine};{Column}{Format.PositionSuffix.value}"
                + BlankLine, end = "")


def ShowCursor(
    IsVisible = True):
    """
        Show or hide cursor
    """

    print(
        f"{Format.Prefix.value}{Format.CursorVisible.value if IsVisible else Format.CursorInvisible.value}", 
        end = "", 
        flush = True)

    time.sleep(.01)


def PlaceCursorAt(
    Line = 1,
    Column = 1):
    """
        Place cursor at specified position
    """

    print(
        f"{Format.Prefix.value}{Line};{Column}{Format.PositionSuffix.value}", 
        end = "", 
        flush = True)


def _ManageNewLines(
    Text,
    Column = 1):
    """
        Manage new lines (\n) in text
    """

    TextLines = []

    RemainingText = Text
    while RemainingText.find("\n") >= 0:
        NewLineIndex = RemainingText.find("\n")
        AppendLine = RemainingText[:NewLineIndex]
        if AppendLine == "":
            AppendLine = " "
        TextLines.append(AppendLine)
        RemainingText = RemainingText[NewLineIndex + 1:]

    # add last text to text lines
    TextLines.append(RemainingText)

    return TextLines


def _ManageTags(
    TextLines,
    FormatDict):
    """
        Create a list of formatting tags
        Returns Text without formatting and a dictionary of formats
    """

    CurrentCharacterIndex = 0
    NewTextLines = []

    # for each line in TextLines
    for TextLine in TextLines:
        RawText = ""
        NumberOfCharactersToJump = 0
        
        # for each character in text line
        for CharacterIndex, Character in enumerate(TextLine):
            
            if NumberOfCharactersToJump > 0:
                # jump the characters forming the last tag
                NumberOfCharactersToJump -= 1
                continue

            if Character == "[":
                # possible tag start

                TagEnd = TextLine.find("]", CharacterIndex) + 1
                TagInString = TextLine[CharacterIndex:TagEnd].upper()
                TagValues = TagInString.replace("[","").replace("]","").split(";")

                # possible tag detected
                if (TagEnd >= 1 
                    and ((len(TagValues) == 2 and len(TagInString) >= 3 and len(TagInString) <= 5)
                        or (len(TagValues) == 3 and len(TagInString) >= 6 and len(TagInString) <= 8))):
                    # tag seems valid

                    # get colors
                    ForegroundColor = TagValues[0]
                    BackgroundColor = TagValues[1]
                    # get style if provided
                    FormatStyle = TagValues[2] if len(TagValues) == 3 else ""

                    # get format string                
                    FormatString = None
                    if ((ForegroundColor == "" or ForegroundColor in [MyColor.value["Tag"] for MyColor in Color]) 
                    and (BackgroundColor == "" or BackgroundColor in [MyColor.value["Tag"] for MyColor in Color])):
                        # colors are valid
                        if ForegroundColor == "" and BackgroundColor == "":
                            # reset to default
                            FormatString = f"{Format.Prefix.value}{Format.Reset.value}"
                        elif ForegroundColor == "":
                            # change only background color
                            FormatString = f"{Format.Prefix.value}{Format.BackgroundPrefix.value}{[MyColor.value['Format'] for MyColor in Color if MyColor.value['Tag'] == BackgroundColor][0]}{Format.StyleAndColorSuffix.value}"
                        elif BackgroundColor == "":
                            # change only foreground color
                            FormatString = f"{Format.Prefix.value}{Format.ForegroundPrefix.value}{[MyColor.value['Format'] for MyColor in Color if MyColor.value['Tag'] == ForegroundColor][0]}{Format.StyleAndColorSuffix.value}"
                        else:
                            # change both colors
                            FormatString = f"{Format.Prefix.value}{Format.ForegroundPrefix.value}{[MyColor.value['Format'] for MyColor in Color if MyColor.value['Tag'] == ForegroundColor][0]};{Format.BackgroundPrefix.value}{[MyColor.value['Format'] for MyColor in Color if MyColor.value['Tag'] == BackgroundColor][0]}{Format.StyleAndColorSuffix.value}"

                    if FormatStyle in [MyStyle.value["Tag"] for MyStyle in Style]:
                        # add style
                        FormatString += f"{Format.Prefix.value}{[MyStyle.value['Format'] for MyStyle in Style if MyStyle.value['Tag'] == FormatStyle][0]}{Format.StyleAndColorSuffix.value}"

                    if FormatString != "":
                        # add formatting to dictionary with position as key
                        FormatDict[CurrentCharacterIndex + len(RawText)] = FormatString
                        NumberOfCharactersToJump = len(TagInString) - 1
                        # adjust format indexes to compensate tag
                        FormatDict = {
                            (Index - NumberOfCharactersToJump - 1
                            if Index > CurrentCharacterIndex + len(RawText)
                            else Index)
                            :Value
                            for Index, Value 
                            in FormatDict.items() 
                            }


                else:
                    # not a valid tag
                    # add character to raw text
                    RawText += Character

            else:
                # not tag
                # add character to raw text
                RawText += Character

        # update TextLines
        NewTextLines.append(RawText)
        CurrentCharacterIndex += len(RawText)
    
    return (NewTextLines, FormatDict)


def _WrapText(
    TextLines,
    FormatDict,
    JustifyText,
    MaxColumns):
    """
        Split text in lines so it fits in specified width (MaxColumns)
        while keeping formatting (via FormatDict)
    """

    NewTextLines = []
    CurrentCharacterIndex = 0
    CurrentLine = ""

    # for each line in TextLines
    for TextLine in TextLines:
        RemainingText = TextLine

        while len(RemainingText) > 0:

            if (MaxColumns is not None 
                and len(RemainingText) > MaxColumns):
                # a square is specified

                WrapPosition = RemainingText.rfind(" ", 0, MaxColumns + 1) 
                if WrapPosition == -1:
                    # no more wrapping
                    CurrentLine = RemainingText
                    RemainingText = ""
                else:
                    # line wrapped
                    CurrentLine = RemainingText[:WrapPosition]
                    RemainingText = RemainingText[WrapPosition:].lstrip()
                    # adjust format indexes to compensate previous lstrip
                    FormatDict = {
                        (Index - 1 
                        if Index > CurrentCharacterIndex + len(CurrentLine)
                        else Index)
                        :Value
                        for Index, Value 
                        in FormatDict.items() 
                        }
            else:
                # no wrapping
                CurrentLine = RemainingText
                RemainingText = ""

            if MaxColumns is not None:
                # justify text
                CharactersBefore = 0
                CharactersAfter = 0
                if JustifyText == Justify.Left:
                    CharactersAfter = MaxColumns - len(CurrentLine)
                    if CharactersAfter > 0:
                        # adjust format indexes to compensate justifying
                        FormatDict = {
                            (Index + CharactersAfter 
                            if Index >= CurrentCharacterIndex + len(CurrentLine)
                            else Index)
                            :Value
                            for Index, Value 
                            in FormatDict.items() 
                            }
                        CurrentLine = CurrentLine.ljust(MaxColumns)
                if JustifyText == Justify.Right:
                    CharactersBefore = MaxColumns - len(CurrentLine)
                    # adjust format indexes to compensate justifying
                    FormatDict = {
                        (Index + CharactersBefore 
                        if Index > CurrentCharacterIndex
                        else Index)
                        :Value
                        for Index, Value 
                        in FormatDict.items() 
                        }
                    CurrentLine = CurrentLine.rjust(MaxColumns)
                elif JustifyText == Justify.Center:
                    Characters = (MaxColumns - len(CurrentLine))
                    CharactersBefore = Characters // 2
                    CharactersAfter = Characters // 2 if Characters % 2 == 0 else (Characters // 2) + 1
                    # adjust format indexes to compensate justifying
                    FormatDict = {
                        (Index + CharactersBefore 
                        if Index > CurrentCharacterIndex
                        else Index)
                        :Value
                        for Index, Value 
                        in FormatDict.items() 
                        }
                    FormatDict = {
                        (Index + CharactersAfter 
                        if Index >= CurrentCharacterIndex + len(CurrentLine) + CharactersBefore
                        else Index)
                        :Value
                        for Index, Value 
                        in FormatDict.items() 
                        }
                    CurrentLine = CurrentLine.center(MaxColumns)

            NewTextLines.append(CurrentLine)
            CurrentCharacterIndex += len(CurrentLine)

    return (NewTextLines, FormatDict)


def Print(
    Text = "", 
    Line = None, 
    Column = None, 
    JustifyText = Justify.No,
    MaxColumns = None,
    MaxLines = None,
    Speed = PrintSpeed.Instant,
    ClearScreenBefore = False, 
    ResetStyleAfter = True,
    JumpLineAfter = True,
    MakeBeep = False):
    """
        Print rich text
        
        Absolute line and/or column position can be specified
        Can be justify in a square (MaxColumns/MaxLines) with word wrap (from Justify enum)
        Speed can be specified (from PrintSpeed enum)
        Optionally clears screen before printing
        Returns the number of printed lines and the length of the last line
        
        Text can contain tags to change colors during printing with following syntax
        Tags have following syntax
            [Foreground color tag;Background color tag;Style]
            ; between foreground color and background color is mandatory
            ; before style is optional if style is omitted
            if one color is ommited it remains the same
            if both colors are omitted, they reset to console default
            possible tags for colors are :
            B - Black
            R - Red
            G - Green
            Y - Yellow
            U - Blue
            M - Magenta
            C - Cyan
            W - White
            possible tags for styles are :
            SB - Bold (this is very subtle to see)
            SU - Underline
            SI - Inverted (foreground and background colors)
    """
    # if (not _RichConsoleEnabled):
    #     _EnableRichconsole()

    if ClearScreenBefore:
        ClearConsole()
        # print(
        #     f"{__FormatPrefix}{__ClearScreen}",
        #     end = "")

    # to make a beep
    BeepString = "" if not MakeBeep else "\a"

    TextLines = []
    FormatDict = {}

    # manage new lines (\n)
    TextLines = _ManageNewLines(Text, Column)

    # remove tags from text and get format dictionary
    (TextLines, FormatDict) = _ManageTags(TextLines, FormatDict)

    # wrap text to fit in specified area
    (TextLines, FormatDict) = _WrapText(TextLines, FormatDict, JustifyText, MaxColumns)

    CurrentCharacterIndex = 0
    # for each line of text
    for LineIndex, CurrentLine in enumerate(TextLines):
        if LineIndex == 0:
            # absolute positioning
            if Line is None and Column is None:
                # no positioning
                pass
            elif not str(int(Line)).isdigit() or not str(int(Column)).isdigit():
                # position error
                print("*** PrintAt : line and/or column have invalid values")
                return ""
            else:
                # define position
                print(
                    f"{Format.Prefix.value}{int(Line)};{int(Column)}{Format.PositionSuffix.value}",
                    end = "")
            LastLineLength = len(CurrentLine)
        else:
            # move cursor 1 line below
            MoveCursorString = f"{Format.Prefix.value}1{Format.MoveDownSuffix.value}"
            # move cursor left is appropriate
            if Column is not None and str(int(Column)).isdigit():
                MoveCursorString += f"{Format.Prefix.value}{LastLineLength}{Format.MoveLeftSuffix.value}"
            print(MoveCursorString, end = "")

        # print text
        # if Speed == PrintSpeed.Instant:
        #     print(BeepString + Text, end = "", flush = True)
        # else:
        for Letter in CurrentLine:
            # print formatting if any at this position
            
            if CurrentCharacterIndex in FormatDict:
                # apply formatting
                # and replace [Line] with current value (for new position on new line)
                print(
                    FormatDict.pop(
                        CurrentCharacterIndex).replace(
                            "[Line]", 
                            str((Line if Line is not None else 0) + LineIndex)), 
                    end = "", flush = True)

            # print letter
            print(BeepString + Letter, end = "", flush = True)
            CurrentCharacterIndex += 1
            
            # wait
            time.sleep(Speed.value)

        # if MaxColumns == None:
        #     print(f"{Format.Prefix.value}{Line+LineIndex};{Column}{Format.PositionSuffix.value}")
        # else:
        print("", end = "", flush = True)

        # exit loop if text exceeds square
        if MaxLines is not None and LineIndex + 1 == MaxLines:
            if len(FormatDict) > 0:
                # reset format if any formatting
                print(
                    f"{Format.Prefix.value}{Format.Reset.value}", 
                    end = "", 
                    flush = True)
            break

    # reset style if specified
    if ResetStyleAfter:
        print(
            f"{Format.Prefix.value}{Format.Reset.value}", 
            end = "", 
            flush = True)
    
    # jump line after printing if needed
    if JumpLineAfter:
        print()

    # return the number of printed lines and the length of last line 
    return (
        len(TextLines), 
        len(TextLines[-1:][0].strip()) + 1 if len(TextLines) > 0 else 0)



# code to test rich console functions
if __name__ == "__main__":

    import timeit

    # variables
    PosX = 10
    PosY = 21
    Shape = "<-O->"
    ShapeColor = "[G;]"
    FullShape = ShapeColor + Shape + "[;]"

    # functions
    def _TestIntro():
        Print(
            "[C;U] Test des fonctionnalités de RichConsole [;]",
            1, 1,
            Speed = PrintSpeed.VeryFast,
            ClearScreenBefore = True,
            MakeBeep = True)
        time.sleep(1)

    def _CursorTest():
        ShowCursor()
        Print(
            "Curseur visible",
            3, 1,
            Speed = PrintSpeed.Medium)
        ShowCursor(False)
        time.sleep(1)
        Print(
            "Curseur invisible",
            3, 30,
            Speed = PrintSpeed.Medium)

    def _SquareTest():
        Print(
            "Texte dans un rectangle : \"[M;]Ce texte s'imprime [Y;]justifié à gauche[M;]/[Y;]centré[M;]/[Y;]justifié à droite[M;] dans un rectangle de [B;W]20[M;B]x[B;W]6[M;B].\nAvec une [G;]marge[M;] de 1 caractère à gauche et à droite.[;]\"",
            5, 1)

        Print(
            "┌──────────────────────┐ │                      │ │                      │ │                      │ │                      │ │                      │ │                      │ └──────────────────────┘",
            8, 5,
            MaxColumns = 24,
            MaxLines = 8)
        Print(
            "[M;]Ce texte s'imprime [Y;]justifié à gauche[M;] dans un rectangle de [B;W]20[M;B]x[B;W]6[M;B].\nAvec une [G;]marge[M;] de 1 caractère à gauche et à droite.[;]",
            9, 7,
            JustifyText = Justify.Left,
            MaxColumns = 20,
            MaxLines = 6,
            Speed = PrintSpeed.UltraFast)

        Print(
            "┌──────────────────────┐ │                      │ │                      │ │                      │ │                      │ │                      │ │                      │ └──────────────────────┘",
            8, 35,
            MaxColumns = 24,
            MaxLines = 8)
        Print(
            "[M;]Ce texte s'imprime [Y;]centré[M;] dans un rectangle de [B;W]20[M;B]x[B;W]6[M;B].\nAvec une [G;]marge[M;] de 1 caractère à gauche et à droite.[;]",
            9, 37,
            JustifyText = Justify.Center,
            MaxColumns = 20,
            MaxLines = 6,
            Speed = PrintSpeed.UltraFast)

        Print(
            "┌──────────────────────┐ │                      │ │                      │ │                      │ │                      │ │                      │ │                      │ └──────────────────────┘",
            8, 65,
            MaxColumns = 24,
            MaxLines = 8)
        Print(
            "[M;]Ce texte s'imprime [Y;]justifié à droite[M;] dans un rectangle de [B;W]20[M;B]x[B;W]6[M;B].\nAvec une [G;]marge[M;] de 1 caractère à gauche et à droite.[;]",
            9, 67,
            JustifyText = Justify.Right,
            MaxColumns = 20,
            MaxLines = 6,
            Speed = PrintSpeed.UltraFast)

    def _AnimationTest():
        Print(
            f"\nUn {FullShape} va se déplacer sur l'écran",
            17, 0)
        _PrintShape()
        Print("[B;Y;SU] Entrée pour démarrer [;]", 19, 0)
        Print("---------------------------------------------------", 32, 0)
        input()
        while PosX <= 40:
            _MoveShape(1, 0)
        while PosY <= 30:
            _MoveShape(0, 1)
        while PosX >= 3:
            _MoveShape(-1, 0)
        while PosY >= 24:
            _MoveShape(0, -1)
        while PosY <= 28:
            _MoveShape(1, .5)

    def _TestEnd():
        Print(
            "[;]Et voilà, [U;]un [G;]petit [R;]tour[;] et c'est fini [Y;]:-)[;]",
            Line = 33, Column = 1)
        Print("À [U;]pluche[;] !")
        ShowCursor()
        print("...\n")

    def _PrintShape():
        Print(
            FullShape, 
            PosY, PosX, 
            JumpLineAfter = False)

    def _MoveShape(DeltaX, DeltaY, XMoveSleep = .01, YMoveSleep = .05):
        global PosX, PosY
        # delete shape at previous position
        Print(
            "".ljust(len(Shape)), 
            PosY, PosX, 
            JumpLineAfter = False)
        # calculate new shape position
        PosX += DeltaX
        PosY += DeltaY
        # draw shape at new position
        _PrintShape()
        # wait
        SleepTime = XMoveSleep
        if DeltaY != 0:
            SleepTime = YMoveSleep
        time.sleep(SleepTime)

    # code
    ClearConsole()
    # input("\nTaper Entrée pour démarrer la démo... ")
    _TestIntro()
    _CursorTest()
    # StartTime = time.time()
    _SquareTest()
    # EndTime = time.time()
    # print("\n\nTemps pour le test Square : ", EndTime - StartTime)
    _AnimationTest()
    _TestEnd()