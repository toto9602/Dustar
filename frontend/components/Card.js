import React from "react";
import { View, Text, Image, StyleSheet } from "react-native";

export default function Card({ content }) {
  return (
    <View style={styles.card}>
      <Image style={styles.cardImage} source={{ uri: content.image }} />
      <View style={styles.cardText}>
        <Text style={styles.cardTitle} numberOfLines={1}>
          {content.title}
        </Text>
        <Text style={styles.cardDesc} numberOfLines={3}>
          {content.desc}
        </Text>
        <Text style={styles.cardDate}>{content.date}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    flex: 1,
    //컨텐츠들을 가로로 나열
    //세로로 나열은 column <- 디폴트 값
    flexDirection: "row",
    justifyContent: "center",
    margin: 10,
    width: "85%",
    borderBottomWidth: 0.5,
    borderBottomColor: "#eee",
    borderRadius: 20,
    padding: 10,
    backgroundColor: "white",
    shadowColor: "#C4C4C4",
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  cardImage: {
    flex: 1,
    width: 100,
    height: 100,
    borderRadius: 50,
  },
  cardText: {
    flex: 2,
    flexDirection: "column",
    marginLeft: 10,
  },
  cardTitle: {
    fontSize: 20,
    fontWeight: "700",
  },
  cardDesc: {
    fontSize: 15,
  },
  cardDate: {
    fontSize: 10,
    color: "#A6A6A6",
  },
});
