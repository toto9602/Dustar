import React from "react";
import { View, Text, Image, StyleSheet, TextInput } from "react-native";

export default function Input() {
  handleEmail = (text) => {
    this.setState({ email: text });
  };

  handlePassword = (text) => {
    this.setState({ password: text });
  };

  return (
    <View style={styles.inputContainer}>
      <Text style={styles.fieldLabel}>이메일</Text>
      <TextInput
        style={styles.input}
        placeholder="meonji@naver.com"
        placeholderTextColor="#707070"
        autoCapitalize="none"
        onChangeText={this.handleEmail}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  inputContainer: {
    flexDirection: "row",
    justifyContent: "center",
  },
  fieldLabel: {
    fontSize: 20,
    fontWeight: "500",
    marginTop: 50,
    marginLeft: 20,
  },
  input: {
    margin: 15,
    width: "60%",
    height: 65,
    backgroundColor: "#E5E5E5",
    borderColor: "transparent",
    borderRadius: 10,
    borderWidth: 1,
  },
  submitButton: {
    backgroundColor: "#A489E7",
    borderRadius: 80,
    padding: 10,
    margin: 15,
    width: "80%",
    height: 80,
    justifyContent: "center",
  },
});
