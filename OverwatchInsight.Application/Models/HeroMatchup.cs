using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OverwatchInsight.Application.Models;

public record HeroMatchup(
        string HeroName,
        int MatchupValue
    )
{

}
