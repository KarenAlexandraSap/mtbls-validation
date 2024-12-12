package metabolights.validation.v2_summary

import rego.v1


# section_messages(source, section, messages) := {key: messages_list |
# 	key := section
# 	messages_list = {msg | some j; messages[j].section == section; messages[j].source == source; msg := messages[j]}
# }

# phase1_files_and_messages := {source: sections |
# 	some i, t

# 	sources = {x.source | x := phase1_all_messages[_]}
# 	source := sources[i]
# 	sections = {section_messages(source, x.section, phase1_all_messages) | phase1_all_messages[t].source == source; x := phase1_all_messages[t]}
# }

# phase1_section_messages := {section: messages |
# 	some i, j
# 	sections = {x.section | x := phase1_all_messages[_]}
# 	sections[i]
# 	section = sections[i]
# 	messages = {x | phase1_all_messages[j].section == section; x := phase1_all_messages[j]}
# }

phase1_all_messages contains result if {
	some rule, _ in data.metabolights.validation.v2.phase1.violations
	startswith(rule, "rule_")
	some result in data.metabolights.validation.v2.phase1.violations[rule]
}


# phase2_files_and_messages := {source: sections |
# 	some i, t

# 	sources = {x.source | x := phase2_all_messages[_]}
# 	source := sources[i]
# 	sections = {section_messages(source, x.section, phase2_all_messages) | phase2_all_messages[t].source == source; x := phase2_all_messages[t]}
# }

# phase2_section_messages := {section: messages |
# 	some i, j
# 	sections = {x.section | x := phase2_all_messages[_]}
# 	sections[i]
# 	section = sections[i]
# 	messages = {x | phase2_all_messages[j].section == section; x := phase2_all_messages[j]}
# }

phase2_all_messages contains result if {
	some i, j
	data.metabolights.validation.v2.phase2[i]
	startswith(i, "rule_")
	result := data.metabolights.validation.v2.phase2.violations[i][j]
}

# phase3_files_and_messages := {source: sections |
# 	some i, t

# 	sources = {x.source | x := phase3_all_messages[_]}
# 	source := sources[i]
# 	sections = {section_messages(source, x.section, phase3_all_messages) | phase3_all_messages[t].source == source; x := phase3_all_messages[t]}
# }

# phase3_section_messages := {section: messages |
# 	some i, j
# 	sections = {x.section | x := phase3_all_messages[_]}
# 	sections[i]
# 	section = sections[i]
# 	messages = {x | phase3_all_messages[j].section == section; x := phase3_all_messages[j]}
# }

phase3_all_messages contains result if {
	some i, j
	data.metabolights.validation.v2.phase3.violations[i]
	startswith(i, "rule_")
	result := data.metabolights.validation.v2.phase3.violations[i][j]
}

# phase4_files_and_messages := {source: sections |
# 	some i, t

# 	sources = {x.source | x := phase4_all_messages[_]}
# 	source := sources[i]
# 	sections = {section_messages(source, x.section, phase4_all_messages) | phase3_all_messages[t].source == source; x := phase4_all_messages[t]}
# }

# phase4_section_messages := {section: messages |
# 	some i, j
# 	sections = {x.section | x := phase4_all_messages[_]}
# 	sections[i]
# 	section = sections[i]
# 	messages = {x | phase4_all_messages[j].section == section; x := phase4_all_messages[j]}
# }

phase4_all_messages contains result if {
	some i, j
	data.metabolights.validation.v2.phase4.violations[i]
	startswith(i, "rule_")
	result := data.metabolights.validation.v2.phase4.violations[i][j]
}


all_messages contains message if {

	some phase in {"phase1", "phase2", "phase3", "phase4"}
	some rule_pack, phase_rules in data.metabolights.validation.v2
	some rule_name, rule_list in phase_rules.violations
	startswith(rule_name, "rule_")
	some message in rule_list
}

all_error_messages contains message if {

	some phase in {"phase1", "phase2", "phase3", "phase4"}
	some rule_pack, phase_rules in data.metabolights.validation.v2
	some rule_name, rule_list in phase_rules.violations
	startswith(rule_name, "rule_")
	some message in rule_list
	message.type == "ERROR"
}