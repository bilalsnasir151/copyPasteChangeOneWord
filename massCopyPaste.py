def replace_word_in_code(code, old_word, new_words):
    copies = []
    for new_word in new_words:
        modified_code = code.replace(old_word, new_word)
        copies.append(modified_code)
    return copies

# Input your code snippet here
original_code = """

	zenaDark: StyleSheet.create({
		accent: Colors.zenaDark.Accent,

		container: {
			flex: 1,
			backgroundColor: Colors.zenaDark.Background,
			paddingTop: 10,
			paddingBottom: 45,
		},
		deleteButton: {
			backgroundColor: "red",
			borderRadius: 50,
			padding: 10,
			alignItems: "center",
			justifyContent: "center",
			marginBottom: 10,
			height: 40,
			width: "49%",
		},
		confirmButton: {
			backgroundColor: "green",
			borderRadius: 50,
			padding: 10,
			justifyContent: "center",
			height: 40,
			alignItems: "center",
			marginBottom: 10,
			width: "49%",
		},
		closeButton: {
			backgroundColor: Colors.zenaDark.Cards,
			borderRadius: 50,
			justifyContent: "center",
			alignItems: "center",
			width: "100%",
			height: 40,
			marginBottom: 10,
		},
		buttonText: {
			color: Colors.zenaDark.PrimaryText,
			fontWeight: "bold",
		},
		textBox: {
			flex: 1,
			flexDirection: "column",
			alignItems: "flex-start",
		},
		selectedDate: {
			flexDirection: "row",
			alignItems: "center",
			marginHorizontal: 8,
			paddingHorizontal: 16,
			height: 50,
			backgroundColor: Colors.zenaDark.Cards,
			borderRadius: 15,
			shadowColor: Colors.zenaDark.Accent, // Add shadow properties for iOS
			shadowOffset: {
				width: 0,
				height: 2,
			},
			shadowOpacity: 0.6,
			shadowRadius: 10,
		},
		searchParametersButton: {
			flexDirection: "row",
			alignItems: "center",
			margin: 8,
			padding: 16,
			backgroundColor: Colors.zenaDark.Cards,
			borderRadius: 15,
			shadowColor: Colors.zenaDark.Accent, // Add shadow properties for iOS
			shadowOffset: {
				width: 0,
				height: 2,
			},
			shadowOpacity: 0.6,
			shadowRadius: 10,
		},

		taskItem: {
			flexDirection: "row",
			alignItems: "center",
			marginVertical: 8,
			marginHorizontal: 8,
			paddingTop: 12, // Add top padding for spacing
			paddingBottom: 12, // Add bottom padding for spacing
			paddingHorizontal: 16,
			backgroundColor: Colors.zenaDark.Cards,
			borderRadius: 15,
			flex: 1, // Allow the task item to stretch vertically
			elevation: 8, // Add elevation for shadow on Android
			shadowColor: "#000", // Add shadow properties for iOS
			shadowOffset: {
				width: 0,
				height: 2,
			},
			shadowOpacity: 0.5,
			shadowRadius: 4,
		},
		optionContainer: {
			padding: 10,
			alignItems: "flex-start",
			flexDirection: "row",
		},
		optionStyle: {
			fontSize: 20,
			textAlign: "center",
			fontWeight: "bold",
			color: Colors.zenaDark.PrimaryText,
		},
		taskItemCompleted: {
			flexDirection: "row",
			alignItems: "center",
			marginVertical: 8,
			marginHorizontal: 8,
			paddingTop: 12, // Add top padding for spacing
			paddingBottom: 12, // Add bottom padding for spacing
			paddingHorizontal: 16,
			backgroundColor: "green",
			borderRadius: 15,
			flex: 1, // Allow the task item to stretch vertically
			elevation: 8, // Add elevation for shadow on Android
			shadowColor: "#000", // Add shadow properties for iOS
			shadowOffset: {
				width: 0,
				height: 2,
			},
			shadowOpacity: 0.5,
			shadowRadius: 4,
		},
		taskItemOverdue: {
			flexDirection: "row",
			alignItems: "center",
			marginVertical: 8,
			marginHorizontal: 8,
			paddingTop: 12, // Add top padding for spacing
			paddingBottom: 12, // Add bottom padding for spacing
			paddingHorizontal: 16,
			backgroundColor: "red",
			borderRadius: 15,
			flex: 1, // Allow the task item to stretch vertically
			elevation: 8, // Add elevation for shadow on Android
			shadowColor: "#000", // Add shadow properties for iOS
			shadowOffset: {
				width: 0,
				height: 2,
			},
			shadowOpacity: 0.5,
			shadowRadius: 4,
		},
		taskName: {
			fontSize: 16,
			fontWeight: "bold",
			color: Colors.zenaDark.PrimaryText,
		},
		taskGroupName: {
			fontSize: 14,
			color: Colors.zenaDark.Accent,
			fontWeight: "bold",
			elevation: 8, // Add elevation for shadow on Android
			shadowColor: "#000", // Add shadow properties for iOS
			shadowOffset: {
				width: 0,
				height: 2,
			},
			shadowOpacity: 0.5,
			shadowRadius: 4,
		},
		taskDescription: {
			fontSize: 14,
			color: Colors.zenaDark.SecondaryText,
		},
		taskDeadline: {
			alignItems: "flex-end",
			marginLeft: 10,
			marginRight: 10,
		},
		taskDate: {
			fontSize: 16,
			fontWeight: "bold",
			color: Colors.zenaDark.PrimaryText,
		},
		taskTime: {
			fontSize: 12,
			color: Colors.zenaDark.SecondaryText,
		},
		headerContainer: {
			flexDirection: "row",
			alignItems: "stretch",
			paddingHorizontal: 16,
			paddingBottom: 8,
			marginTop: 50,
		},
		header: {
			flex: 1,
		},
		addInputContainer: {
			alignItems: "flex-end",
			paddingRight: 8,
			flex: 1,
		},
		modalView: {
			backgroundColor: Colors.zenaDark.Menu,
			borderTopStartRadius: 15,
			borderTopEndRadius: 15,
			padding: 10,
			alignItems: "flex-start",
			shadowColor: "#000",
			shadowOffset: {
				width: 0,
				height: 2,
			},
			shadowOpacity: 0.5,
			shadowRadius: 4,
			elevation: 5,
			position: "absolute",
			bottom: 0,
			left: 0,
			right: 0,
			flex: 1,
		},
		labelButton: {
			flexDirection: "row",
			alignItems: "center",
			marginVertical: 8,
			marginHorizontal: 8,
			paddingTop: 8, // Add top padding for spacing
			paddingBottom: 8, // Add bottom padding for spacing
			padding: 12,
			backgroundColor: Colors.zenaDark.Cards,
			borderRadius: 10,
			shadowColor: Colors.zenaDark.Accent, // Add shadow properties for iOS
			shadowOffset: {
				width: 0,
				height: 2,
			},
			shadowOpacity: 0.5,
			shadowRadius: 4,
		},
		addGroupItem: {
			flexDirection: "row",
			alignItems: "center",
			justifyContent: "center",
			marginVertical: 8,
			marginHorizontal: 8,
			paddingTop: 8, // Add top padding for spacing
			paddingBottom: 8, // Add bottom padding for spacing
			backgroundColor: Colors.zenaDark.Cards,
			borderRadius: 15,
			shadowColor: Colors.zenaDark.Accent, // Add shadow properties for iOS
			shadowOffset: {
				width: 0,
				height: 2,
			},
			shadowOpacity: 0.5,
			shadowRadius: 4,
		},
		closeGroupItem: {
			flexDirection: "row",
			alignItems: "center",
			justifyContent: "center",
			marginVertical: 8,
			marginHorizontal: 8,
			paddingTop: 8, // Add top padding for spacing
			paddingBottom: 8, // Add bottom padding for spacing
			backgroundColor: Colors.zenaDark.Cards,
			borderColor: 'red',
			borderWidth: 2,
			borderRadius: 15,
			shadowColor: 'red', // Add shadow properties for iOS
			shadowOffset: {
				width: 0,
				height: 2,
			},
			shadowOpacity: 0.5,
			shadowRadius: 4,
		},
		plusButton: {
			fontSize: 20,
			color: Colors.zenaDark.Accent,
			fontWeight: "bold",
		},
		buttonContainer: {
			width: "100%",
			flexDirection: "row",
			justifyContent: "space-between",
			alignContent: "center",
			alignItems: "flex-end",
			paddingTop: 10,
			paddingHorizontal: 10,
		},
		joinButton: {
			backgroundColor: Colors.zenaDark.Cards,
			borderRadius: 10,
			padding: 10,
			alignItems: "center",
			marginBottom: 10,
			height: 40,
			width: "49%",
		},
	}),

"""

# Input the word to be replaced
old_word = "zenaDark"

# Input the list of new words separated by spaces
new_words_input = "stellar bloom USALight USADark landScapeLight landScapeDark pastelPink pastelPurple love nauticalDark nauticalLight jedi sith OG pandaLight pandaDark"
new_words = new_words_input.split()

modified_codes = replace_word_in_code(original_code, old_word, new_words)

# Printing the modified code
print("\n".join(modified_codes))
