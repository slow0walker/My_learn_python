import json
class GameStats:
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        #  保存最高分
        self.high_score = self._read_high_score()

    def reset_stats(self):
        """初始化随游戏进行可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    # GPT
    def _read_high_score(self):
        """Read the high score from a file."""
        try:
            with open('high_score.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Save the high score to a file."""
        with open('high_score.json', 'w') as file:
            json.dump(self.high_score, file)