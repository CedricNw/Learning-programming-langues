<template>
  <div class="game" style="margin: 2em;">
    <h1>Tic Tac Toe</h1>

    <div v-if="!won" class="game-board">
      <div v-for="(row, rowIndex) in board" :key="rowIndex" class="row">
        <div
          v-for="(cell, colIndex) in row"
          :key="colIndex"
          class="white-box"
          @click="placePlayersLetter(rowIndex, colIndex)"
        >
          <h2 class="letter" style="color:black">{{ cell }}</h2>
        </div>
      </div>
    </div>

    <div v-else>
      <h2>{{ winner }} hat gewonnen!</h2>
      <div class="restart" @click="restart">Restart</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      won: false,
      winner: "",
      board: [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
      ],
      currentPlayer: "X"
    }
  },
  methods: {
    placePlayersLetter(row, col) {
      // Wenn Feld bereits belegt, nichts tun
      if (this.board[row][col] !== "" || this.won) return

      // Feld mit aktuellem Symbol füllen
      this.board[row][col] = this.currentPlayer

      // Prüfen, ob jemand gewonnen hat
      this.checkHasWon()

      // Nur Spieler wechseln, wenn noch niemand gewonnen hat
      if (!this.won) {
        this.currentPlayer = this.currentPlayer === "X" ? "O" : "X"
      }
    },

    checkHasWon() {
      const b = this.board
      const p = this.currentPlayer

      // Zeilen und Spalten prüfen
      for (let i = 0; i < 3; i++) {
        if (b[i][0] === p && b[i][1] === p && b[i][2] === p) {
          this.won = true
          this.winner = p
          return
        }
        if (b[0][i] === p && b[1][i] === p && b[2][i] === p) {
          this.won = true
          this.winner = p
          return
        }
      }

      // Diagonalen prüfen
      if (b[0][0] === p && b[1][1] === p && b[2][2] === p) {
        this.won = true
        this.winner = p
        return
      }
      if (b[0][2] === p && b[1][1] === p && b[2][0] === p) {
        this.won = true
        this.winner = p
        return
      }
    },

    restart() {
      this.won = false
      this.winner = ""
      this.board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
      ]
      this.currentPlayer = "X"
    }
  }
}
</script>

<style scoped>

.game-board {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.row {
  display: flex;
  gap: 1rem;
}

.white-box {
  width: 5rem;
  height: 5rem;
  background-color: white;
  border: 2px solid black;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.restart {
  margin-top: 2rem;
  padding: 0.5rem 1rem;
  border: 1px solid hsla(160, 100%, 37%, 1);;
  cursor: pointer;
  color: hsla(160, 100%, 37%, 1);
  display: inline-block;
  border-radius: 15px;
}
</style>
