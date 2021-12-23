import React from "react";
import { StyleSheet, Text, View, TouchableOpacity, Alert } from "react-native";

export default function DetailPage() {
  const popup = () => {
    Alert.alert("팝업!!");
  };
  return (
    <View style={styles.container}>
      <View style={styles.textContainer}>
        <Text style={styles.desc3}>
          때로는 귀엽고 하찮은 당신은, 어떤 먼지일까요?
        </Text>
        <TouchableOpacity style={styles.button} onPress={() => popup()}>
          <Text style={styles.buttonText}>테스트하러 가기</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "white",
  },
  textContainer: {
    justifyContent: "center",
    alignItems: "center",
  },
  desc3: {
    marginTop: "10%",
    marginBottom: "10%",
    color: "black",
  },
  button: {
    width: 100,
    marginBottom: "10%",
    padding: 10,
    borderWidth: 1,
    backgroundColor: "rgba(41, 25, 101, 0.8)",
    borderRadius: 20,
  },
  buttonText: {
    color: "#fff",
    textAlign: "center",
    borderColor: "rgba(41, 25, 101, 0.8)",
  },
});
