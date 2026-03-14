import json
from openai import OpenAI

class LLMPlayer:
    
    def __init__(self, llm_base_url, model, api_key, mark):
        self.model = model
        self.mark = mark
        self.client = OpenAI(base_url=llm_base_url, api_key=api_key)

        self.system_prompt = f"""
You are a Connect Four player.

You are playing as: {mark}

Board representation:
- 6 rows
- 7 columns
- columns indexed 0–6
- pieces drop downward

Symbols:
X = player X
O = player O
. = empty

Your job:
1. Analyze the board
2. Identify threats (yours and opponent)
3. Explain your strategy
4. Choose a legal move

Respond ONLY in JSON with the format:

{{
  "assessment": "...",
  "threats": "...",
  "strategy": "...",
  "move": <column_number>
}}
"""
        
    def build_user_prompt(self, board_state):

        return f"""
Current board state:

{json.dumps(board_state, indent=2)}

You are player {self.mark}.

Choose your move.
"""
    
    def make_move(self, board):

        state = board.to_llm_json()

        print("Player" + self.mark + " is thinking...")

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.build_user_prompt(state)}
            ],
            response_format={"type": "json_object"}
        )

        output = json.loads(response.choices[0].message.content)

        return output
