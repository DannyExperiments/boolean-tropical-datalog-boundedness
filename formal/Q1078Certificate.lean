import Std

namespace TropicalRounds

def minWithInfinity : Option Nat → Option Nat → Option Nat
  | none, right => right
  | left, none => left
  | some a, some b => some (min a b)

def target (n : Nat) : Nat → Nat → Option Nat
  | 0, _ => none
  | 1, _ => none
  | round + 2, i =>
    let w := 3 ^ (n - i)
    let previous := if i < n then (target n (round + 1) (i + 1)).map (w + ·) else none
    minWithInfinity (some (2 * w)) previous

theorem depth_trace : (List.range 8).map (fun r => target 4 r 0) =
    [none, none, some 162, some 135, some 126, some 123, some 122, some 122] := by
  decide +kernel

theorem later_stop_improves (pathCost w : Nat) (positive : 0 < w) :
    pathCost + 3 * w + 2 * w < pathCost + 2 * (3 * w) := by
  omega

theorem zero_test (a b : Nat) : a + b ≤ 0 ↔ a ≤ 0 ∧ b ≤ 0 := by omega

theorem one_test (a b : Nat) :
    a + b ≤ 1 ↔ (a ≤ 0 ∧ b ≤ 1) ∨ (a ≤ 1 ∧ b ≤ 0) := by omega

theorem boolean_absorption (guard recursive : Bool) :
    (guard && (guard || recursive)) = guard := by
  cases guard <;> cases recursive <;> decide

#print axioms depth_trace
#print axioms later_stop_improves
#print axioms zero_test
#print axioms one_test
#print axioms boolean_absorption

end TropicalRounds
